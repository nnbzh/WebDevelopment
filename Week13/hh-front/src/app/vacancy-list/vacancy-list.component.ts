import { Component, OnInit } from '@angular/core';
import {VacancyService} from '../vacancy.service';
import {Vacancy} from '../models';
import {ActivatedRoute} from '@angular/router';



@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
  constructor(public vacancyService: VacancyService, private route: ActivatedRoute,
) { }
  vacancies: Vacancy[] = [];
  ngOnInit(): void {
    this.getVacancies();
  }
  getVacancies() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.vacancyService.getVacancies(id).subscribe(vacancies => {this.vacancies = vacancies; });
  }


}
