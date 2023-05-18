class tarjeta extends Payment {
    constructor (id, franquicia, cvv, FDV){
        super (id)
        this.franquicia = franquicia;
        this.FDV        = FDV;
        this. cvv       = cvv;
    }
}