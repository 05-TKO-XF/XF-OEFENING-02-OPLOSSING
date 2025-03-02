from django import forms
from django.core.mail import send_mail
from datetime import datetime
from django.core.validators import RegexValidator

class Email(forms.Form):
    frmNaam = forms.CharField(min_length=3,max_length=50)
    frmEmail = forms.EmailField()
    frmTelefoon = forms.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex="^(((\+|00)\d{2}\s?)|0){1}\d{3}\s?\d{3}\s?\d{3}$",
                message="Ongeldige telefoonnummer",
                code="ongeldig telefoon nummer",
            ),
        ],
    )
    frmBericht = forms.CharField(
        required = True,
        widget = forms.Textarea
    )
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # add custom error messages
        self.fields['frmNaam'].error_messages.update({
            'required': 'Naam is een vereist veld',
            'max_length': 'Naam telt maximaal 50 karakters',
            'min_length': 'Naam telt minstens 3 karakters'
        })

        self.fields['frmEmail'].error_messages.update({
            'required': 'E-mail is een verplicht veld',
        })

        self.fields['frmTelefoon'].error_messages.update({
            'required': 'Telefoon is een vereist veld'
        })

        self.fields['frmBericht'].error_messages.update({
            'required': 'Bericht is een verplicht veld'
        })

    def mail(self, frmDta):
        tijdstip = datetime.now().strftime('%d-%m-%Y %H:%M')
        aan = ['oocmsdi@gmail.com']
        van = 'noreply@gmail.com'
        
        berichtTekst = f'''
            Contactformulier
            ------------------------------
            verzonder op: {tijdstip}\r
            van: {frmDta['frmNaam']}\r
            email: {frmDta['frmEmail']}\r
            telefoon: {frmDta['frmTelefoon']}\r
            bericht:\r
            {frmDta['frmBericht']}
        '''

        berichtHTML = f'''
                <h1>Contactformulier</h1>
                <p>verzonden op: <strong>{tijdstip}</strong></p>
                <p>van: <strong>{frmDta['frmNaam']}</strong></p>
                <p>email: <strong><a href="mailto:{frmDta['frmEmail']}">{frmDta['frmEmail']}</a></strong></p>
                <p>mobiel: <strong>{frmDta['frmTelefoon']}</strong></p>
                <p>boodschap:<br>{frmDta['frmBericht']}</p>
            '''
        
        if send_mail(
                subject = 'bericht contactformulier',
                message = berichtTekst,
                html_message = berichtHTML,
                from_email = van,
                recipient_list = aan,
                fail_silently = True
            ):
            return True
        else:
            return False
