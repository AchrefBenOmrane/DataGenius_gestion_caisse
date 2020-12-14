import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';



import { AppComponent } from './app.component';
import { ShoppingComponent } from './shopping/shopping.component';
import { OrdersComponent } from './shopping/orders/orders.component';
import { ProductsComponent } from './shopping/products/products.component';
import { ShoppingCartComponent } from './shopping/shopping-cart/shopping-cart.component';
import { EcommerceService } from './shopping/services/ecommerce-service.service';
import { AddProductComponent } from './shopping/add-product/add-product.component';

@NgModule({
  declarations: [
    AppComponent,
    ShoppingComponent,
    OrdersComponent,
    ProductsComponent,
    ShoppingCartComponent,
    AddProductComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule 
  ],
  providers: [EcommerceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
