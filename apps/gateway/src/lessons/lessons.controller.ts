import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  UseGuards,
  Request,
} from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiBearerAuth } from '@nestjs/swagger';
import { LessonsService } from './lessons.service';
import { JwtAuthGuard } from '../auth/jwt-auth.guard';

@ApiTags('Lessons')
@Controller('lessons')
@UseGuards(JwtAuthGuard)
@ApiBearerAuth()
export class LessonsController {
  constructor(private readonly lessonsService: LessonsService) {}

  @Post()
  @ApiOperation({ summary: 'Create a new lesson' })
  @ApiResponse({ status: 201, description: 'Lesson created successfully' })
  create(@Body() createLessonDto: any, @Request() req: any) {
    return this.lessonsService.create(createLessonDto, req.user.userId);
  }

  @Get()
  @ApiOperation({ summary: 'Get all lessons' })
  @ApiResponse({ status: 200, description: 'Return all lessons' })
  findAll() {
    return this.lessonsService.findAll();
  }

  @Get(':id')
  @ApiOperation({ summary: 'Get a lesson by id' })
  @ApiResponse({ status: 200, description: 'Return the lesson' })
  findOne(@Param('id') id: string) {
    return this.lessonsService.findOne(id);
  }

  @Patch(':id')
  @ApiOperation({ summary: 'Update a lesson' })
  @ApiResponse({ status: 200, description: 'Lesson updated successfully' })
  update(@Param('id') id: string, @Body() updateLessonDto: any) {
    return this.lessonsService.update(id, updateLessonDto);
  }

  @Delete(':id')
  @ApiOperation({ summary: 'Delete a lesson' })
  @ApiResponse({ status: 200, description: 'Lesson deleted successfully' })
  remove(@Param('id') id: string) {
    return this.lessonsService.remove(id);
  }
}
