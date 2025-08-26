'use client';
import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Download, FileText, FileSpreadsheet, Archive, ExternalLink, CheckCircle, Clock } from 'lucide-react';

interface ExportFile {
  name: string;
  type: string;
  content: string;
  signed_url?: string;
}

interface ExportMetadata {
  lesson_id: string;
  topic: string;
  generated_at: string;
  version: string;
  file_count: number;
  total_size_estimate: number;
  expires_at: string;
}

interface ExportData {
  files: {
    pack_pdf?: string;
    slides_mdx?: string;
    worksheets_docx?: string;
    quiz_pdf?: string;
    csv_grades?: string;
    bundle_zip?: string;
  };
  metadata: ExportMetadata;
  status: string;
}

interface ExportPanelProps {
  exportData: ExportData;
}

export function ExportPanel({ exportData }: ExportPanelProps) {
  const [downloading, setDownloading] = useState<string | null>(null);

  const exportFiles = [
    {
      key: 'pack_pdf',
      name: 'Lesson Pack (PDF)',
      description: 'Complete lesson plan with all components',
      icon: FileText,
      type: 'pdf',
      content: exportData.files.pack_pdf
    },
    {
      key: 'slides_mdx',
      name: 'Slides (MDX)',
      description: 'Presentation slides in MDX format',
      icon: FileText,
      type: 'mdx',
      content: exportData.files.slides_mdx
    },
    {
      key: 'worksheets_docx',
      name: 'Worksheets (DOCX)',
      description: 'Student worksheets and activities',
      icon: FileText,
      type: 'docx',
      content: exportData.files.worksheets_docx
    },
    {
      key: 'quiz_pdf',
      name: 'Quiz (PDF)',
      description: 'Assessment with answer key',
      icon: FileText,
      type: 'pdf',
      content: exportData.files.quiz_pdf
    },
    {
      key: 'csv_grades',
      name: 'Gradebook (CSV)',
      description: 'Gradebook template with student roster',
      icon: FileSpreadsheet,
      type: 'csv',
      content: exportData.files.csv_grades
    },
    {
      key: 'bundle_zip',
      name: 'Complete Bundle (ZIP)',
      description: 'All materials in a single ZIP file',
      icon: Archive,
      type: 'zip',
      content: exportData.files.bundle_zip
    }
  ];

  const handleDownload = async (fileKey: string, fileName: string, content: string) => {
    setDownloading(fileKey);
    try {
      // Create a blob and download
      const blob = new Blob([content], { type: 'text/plain' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = fileName;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (error) {
      console.error('Error downloading file:', error);
    } finally {
      setDownloading(null);
    }
  };

  const formatFileSize = (bytes: number) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleString();
  };

  return (
    <div className="w-full">
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Download className="h-5 w-5" />
            Export Materials
          </CardTitle>
          <div className="text-sm text-gray-600">
            Generated on {formatDate(exportData.metadata.generated_at)} • 
            Version {exportData.metadata.version} • 
            {formatFileSize(exportData.metadata.total_size_estimate)}
          </div>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {exportFiles.map((file) => {
              const Icon = file.icon;
              const isAvailable = file.content && file.content.length > 0;
              
              return (
                <Card key={file.key} className="border-2 hover:border-blue-300 transition-colors">
                  <CardContent className="p-4">
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex items-center gap-2">
                        <Icon className="h-5 w-5 text-blue-600" />
                        <div>
                          <h3 className="font-medium text-sm">{file.name}</h3>
                          <p className="text-xs text-gray-600">{file.description}</p>
                        </div>
                      </div>
                      {isAvailable ? (
                        <CheckCircle className="h-4 w-4 text-green-500" />
                      ) : (
                        <Clock className="h-4 w-4 text-gray-400" />
                      )}
                    </div>
                    
                    <div className="flex items-center justify-between">
                      <Badge variant={isAvailable ? "default" : "secondary"}>
                        {file.type.toUpperCase()}
                      </Badge>
                      
                      {isAvailable ? (
                        <Button
                          size="sm"
                          onClick={() => handleDownload(
                            file.key, 
                            `${file.name.toLowerCase().replace(/\s+/g, '_')}.${file.type}`,
                            file.content
                          )}
                          disabled={downloading === file.key}
                        >
                          {downloading === file.key ? (
                            'Downloading...'
                          ) : (
                            <>
                              <Download className="h-3 w-3 mr-1" />
                              Download
                            </>
                          )}
                        </Button>
                      ) : (
                        <Button size="sm" variant="outline" disabled>
                          Not Available
                        </Button>
                      )}
                    </div>
                  </CardContent>
                </Card>
              );
            })}
          </div>

          <div className="mt-6 p-4 bg-blue-50 rounded-lg">
            <h4 className="font-medium text-blue-900 mb-2">Export Information</h4>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
              <div>
                <span className="text-blue-700">Lesson ID:</span>
                <p className="font-mono text-xs">{exportData.metadata.lesson_id}</p>
              </div>
              <div>
                <span className="text-blue-700">Files:</span>
                <p>{exportData.metadata.file_count} total</p>
              </div>
              <div>
                <span className="text-blue-700">Expires:</span>
                <p>{formatDate(exportData.metadata.expires_at)}</p>
              </div>
              <div>
                <span className="text-blue-700">Status:</span>
                <Badge variant={exportData.status === 'completed' ? 'default' : 'destructive'}>
                  {exportData.status}
                </Badge>
              </div>
            </div>
          </div>

          <div className="mt-4 text-xs text-gray-500">
            <p>• All files are generated in real-time and optimized for classroom use</p>
            <p>• Downloads include proper formatting and accessibility features</p>
            <p>• Files expire after 30 days for security</p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
