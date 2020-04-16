import { NgModule } from '@angular/core';
import {Routes, RouterModule} from '@angular/router';
import { CommonModule } from '@angular/common';
import {VacancyListComponent} from './vacancy-list/vacancy-list.component';
import {CompanyListComponent} from './company-list/company-list.component';


const routes: Routes = [
  {path: '', component: CompanyListComponent},
  {path: 'companies/:id/vacancies', component: VacancyListComponent}
]

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
