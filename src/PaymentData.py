class PaymentData:

    def __init__(self,tarj_VISA,tarj_MASTERCARD,num_tarj,cod_seg,importe):
        self.tarj_VISA = 'VISA'
        self.tarj_MASTERCARD = 'MASTERCARD'
        self.num_tarj = num_tarj
        self.cod_seg = cod_seg
        self.importe = importe
        pass

    def Error_pago(self,tarj_MASTERCARD,tarj_VISA,num_tarj,cod_seg,importe):
        error = False
        if tarj_MASTERCARD == 'MASTERCARD' and tarj_VISA == 'VISA':
            error = True
        if tarj_VISA != 'VISA' and tarj_MASTERCARD != 'MASTERCARD':
            error = True
        if num_tarj == '':
            error = True
        if cod_seg == '':
            error = True
        return error
    pass
        
