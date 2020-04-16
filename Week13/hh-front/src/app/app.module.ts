import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import { CompanyListComponent } from './company-list/company-list.component';
import {FormsModule} from '@angular/forms';
import {AuthInterceptor} from './app.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    VacancyListComponent,
    CompanyListComponent
  ],
  imports: [
    AppRoutingModule,
    FormsModule,
    BrowserModule,
    HttpClientModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
