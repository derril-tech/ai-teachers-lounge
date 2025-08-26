import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class LessonsService {
  constructor(private prisma: PrismaService) {}

  async findAll() {
    return this.prisma.lesson.findMany({
      include: {
        objectives: true,
        sections: true,
        vocab: true,
        misconceptions: true,
        quizzes: {
          include: {
            items: true,
          },
        },
        activities: true,
        inserts: true,
        udlFlags: true,
        createdBy: {
          select: {
            id: true,
            name: true,
            email: true,
          },
        },
      },
    });
  }

  async findOne(id: string) {
    return this.prisma.lesson.findUnique({
      where: { id },
      include: {
        objectives: true,
        sections: true,
        vocab: true,
        misconceptions: true,
        quizzes: {
          include: {
            items: true,
          },
        },
        activities: true,
        inserts: true,
        udlFlags: true,
        createdBy: {
          select: {
            id: true,
            name: true,
            email: true,
          },
        },
      },
    });
  }

  async create(data: any, userId: string) {
    return this.prisma.lesson.create({
      data: {
        ...data,
        createdById: userId,
      },
      include: {
        objectives: true,
        sections: true,
        vocab: true,
        misconceptions: true,
        quizzes: true,
        activities: true,
        inserts: true,
        udlFlags: true,
        createdBy: {
          select: {
            id: true,
            name: true,
            email: true,
          },
        },
      },
    });
  }

  async update(id: string, data: any) {
    return this.prisma.lesson.update({
      where: { id },
      data,
      include: {
        objectives: true,
        sections: true,
        vocab: true,
        misconceptions: true,
        quizzes: {
          include: {
            items: true,
          },
        },
        activities: true,
        inserts: true,
        udlFlags: true,
        createdBy: {
          select: {
            id: true,
            name: true,
            email: true,
          },
        },
      },
    });
  }

  async remove(id: string) {
    return this.prisma.lesson.delete({
      where: { id },
    });
  }
}
