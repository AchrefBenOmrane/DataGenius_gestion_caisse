import { Component, OnInit } from '@angular/core';
import {EcommerceService} from '../services/ecommerce-service.service';
import { Product1 } from "../models/product1.model";

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.css']
})
export class AddProductComponent implements OnInit {
  produit: Product1 = new Product1();
  submitted = false;


  constructor(public service:EcommerceService) {  }

  ngOnInit() {
  }

  save() {
    this.service.create(this.produit)
      .subscribe(
        data => {
          console.log(data);
          this.submitted = true;
        },
        error => console.log(error));
    this.produit = new Product1();
  }
 
  onSubmit() {
    this.save();
  }

}
