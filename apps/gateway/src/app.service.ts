import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'AI Teacher\'s Lounge Gateway is running!';
  }
}
