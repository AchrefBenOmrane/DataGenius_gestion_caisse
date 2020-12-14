export class Product {
    id: number;
    name: string;
    price: number;
    pictureUrl: string;
    quantity: number;

    constructor(id: number, name: string, price: number, pictureUrl: string,quantity: number) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.pictureUrl = pictureUrl;
        this.quantity=quantity;
    }

    
}