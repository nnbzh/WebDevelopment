import { Injectable } from '@angular/core';
import {Observable, of } from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {Vacancy} from './models';

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  constructor(private http: HttpClient) {}
  getVacancies(id): Observable<Vacancy[]> {
    console.log(id);
    return this.http.get<Vacancy[]>(`http://localhost:8000/api/companies/${id}/vacancies`);
  }
}
