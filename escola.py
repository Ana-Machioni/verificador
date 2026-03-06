def verificador_media(media:int|float) ->str:
    """Esta função retorna se o aluno passou ou nao  de ano"""

    # testando p ver se a media é um numero 
    if  not isinstance(media,(int, float)):
        raise TypeError("Tipo invalido, a entrada deve ser numerica")

    if media < 0:
        raise ValueError("O valor deve ser maior ou igual a 0 e menor ou igual a 10")
    
    if media > 10:
        raise ValueError("O valor deve ser maior ou igual a 0 e menor ou igual a 10")
    if media >= 7:
        return "Aprovado"
    elif media < 5:
        return "Reprovado"
    else:
        return "Recuperação"
    
if __name__ =="__main__":
    print(verificador_media(5))
