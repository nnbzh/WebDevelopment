export class Company {
  id: number;
  name: string;
  description: string;
}

export class Vacancy {
  id: number;
  name: string;
  description: string;
  salary: number;
  company_id: number;
}

export class LoginResponse {
  token: string;
}
