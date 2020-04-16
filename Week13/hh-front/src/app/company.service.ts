import { Injectable } from '@angular/core';
import {Observable, of } from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Company, LoginResponse} from './models';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  constructor(private http: HttpClient) {}
  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>('http://localhost:8000/api/companies/');
  }

  login(username, password): Observable<any> {
    return this.http.post('http://localhost:8000/api/login/', {
      username: username,
      password: password
    });
  }
}
