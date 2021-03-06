import {Component, OnInit} from '@angular/core';
import {EcommerceService} from "../services/ecommerce-service.service";
import {Subscription} from "rxjs/internal/Subscription";
import {ProductOrders} from "../models/product-orders.model";
import {Product} from "../models/product.model";

@Component({
    selector: 'app-products',
    templateUrl: './products.component.html',
    styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
    productOrders: Product[] = [];
    products: Product[] = [];
    selectedProductOrder: Product;
    private shoppingCartOrders: ProductOrders;
    sub: Subscription;
    productSelected: boolean = false;
    error:'';

    


    constructor(private ecommerceService: EcommerceService) {
    }

    ngOnInit() {
        this.productOrders = [];
        this.loadProducts();
        this.loadOrders();
    }

    addToCart(order: Product) {
        this.ecommerceService.SelectedProductOrder = order;
        this.selectedProductOrder = this.ecommerceService.SelectedProductOrder;
        this.productSelected = true;
    }

    removeFromCart(productOrder: Product) {
        let index = this.getProductIndex(productOrder);
        if (index > -1) {
            this.shoppingCartOrders.productOrders.splice(
                this.getProductIndex(productOrder), 1);
        }
        this.ecommerceService.ProductOrders = this.shoppingCartOrders;
        this.shoppingCartOrders = this.ecommerceService.ProductOrders;
        this.productSelected = false;
    }

    getProductIndex(product: Product): number {
        return this.ecommerceService.ProductOrders.productOrders.findIndex(value => value===product);
            // (value => value.product === product):;
    }

    isProductSelected(product: Product): boolean {
        return this.getProductIndex(product) > -1;
    }


    loadProducts(){
        this.ecommerceService.getAllProducts().subscribe(
          res=>{
            this.products= res as Product[];
            console.log(res);
            
  
          },
          err=>{this.error=err;
          console.log(err);
          }
        )
      }

    
    loadOrders() {
        this.sub = this.ecommerceService.OrdersChanged.subscribe(() => {
            this.shoppingCartOrders = this.ecommerceService.ProductOrders;
        });
    }

    reset() {
        this.productOrders = [];
        this.loadProducts();
        this.ecommerceService.ProductOrders.productOrders = [];
        this.loadOrders();
        this.productSelected = false;
    }
}