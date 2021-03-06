# zalaczamy "biblioteki", czyli gotowe paczki z funkcjami, ktorych uzyjemy
import os, sys
import pygame
import random

# poczatkowa pozycja zjadacza na ekranie
pozycja_zjadacza_x = 30
pozycja_zjadacza_y = 30

# rozmiar planszy
rozmiar_planszy_x = 800
rozmiar_planszy_y = 800

# definicja kolorow w skali rbg
kolor_ekranu = (10, 150, 10)
kolor_zjadacza = (255, 224, 0)
kolor_tekstu = (10, 10, 10)
kolor_tla_tekstu = (255, 255, 255)

promien_zjadacza = 15
punkty = 0


# funkcja, ktora sprawi, ze zobaczymy w losowym miejscu jedzenie.
# Dzieki temu ze rozwiazanie jest zdefiniowane jako funkcja, bedziemy mogli uzywac go wiele razy, bez kopiowania kodu
def pokaz_jedzenie():
    global pozycja_jedzenia_x
    global pozycja_jedzenia_y
    pozycja_jedzenia_x = random.randint(5, rozmiar_planszy_x - 5)
    pozycja_jedzenia_y = random.randint(5, rozmiar_planszy_y - 5)
    kolor_kulki = (200, 0, 0)
    pygame.draw.circle(screen, kolor_kulki, (pozycja_jedzenia_x, pozycja_jedzenia_y), 3, 0)
    pygame.display.flip()


# funkcja, ktora rusza naszym zjadaczem.
# Ta funkcja przyjmuje zmienne - bedzie wiec dzialac inaczej, w zaleznosci od tego z jakimi liczbami ja wywolamy
def rusz_zjadaczem(zmiana_x, zmiana_y):
    global pozycja_zjadacza_x
    global pozycja_zjadacza_y
    # wymazujemy starego zjadacza, czyli w miejsce zoltej kulki rysujemy kulke w kolorze tla
    pygame.draw.circle(screen, kolor_ekranu, (pozycja_zjadacza_x, pozycja_zjadacza_y), promien_zjadacza, 0)
    # liczymy nowe miejsce zjadacza
    pozycja_zjadacza_x = pozycja_zjadacza_x + zmiana_x
    pozycja_zjadacza_y = pozycja_zjadacza_y + zmiana_y
    # rysujemy nowego zjadacza w nowej pozycji
    pygame.draw.circle(screen, kolor_zjadacza, (pozycja_zjadacza_x, pozycja_zjadacza_y), promien_zjadacza, 0)
    pygame.display.flip()  # tak jak juz to robilismy wczesniej odswiezamy ekran, zeby zobaczyc zmiany


# wyswietlanie punktow
def wyswietl_punkty(ilosc_punktow):
    pygame.draw.rect(screen, kolor_tla_tekstu, (rozmiar_planszy_x - 90, 2, rozmiar_planszy_x, 15), 0)  # tlo dla punktow - zakrywa nam poprzedni text
    pygame.font.init()  # inicjujemy czcionki
    font = pygame.font.Font(None, 24)  # wybieramy domyslna czcionke o rozmiarze 24
    text = font.render("Punkty: %s" % ilosc_punktow, 1, kolor_tekstu)  # chcemy wyswietlic zmienna punkty na ekranie
    screen.blit(text, (rozmiar_planszy_x - 90,
                       2))  # zamiast odswiezania ekranu uzywamy funkcji blit, jej zmienna jest pozycja w ktorej chcemy zamiescic tekst


# przygotowujemy poczatkowy ekran gry:
screen = pygame.display.set_mode((rozmiar_planszy_x, rozmiar_planszy_y))  # przygotowanie nowego ekranu o wymiarach 600x600
pygame.display.set_caption('Zjadacz')  # ustawiamy etykietke okna
screen.fill(kolor_ekranu)  # wypelniamy ekran kolorem zielonym
pokaz_jedzenie()  # pokazujemy pierwsza kropke do zjedzenia
pygame.display.flip()  # odswiezamy ekran, zeby zobaczyc zmiany, ktore wprowadzilismy powyzej
wyswietl_punkty(punkty) #wyswietlenie poczatkowej liczby punktow
rusz_zjadaczem(0, 0) # wyswietlamy zjadacza przed rozpoczeciem

# obsluga programu za pomoca klawiatury - tu mowimy programowi co ma zrobic jesli zostanie nacisniety ktorys przycisk
running = True
while running:
    wyswietl_punkty(punkty)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        rusz_zjadaczem(0, 1)
    if ((pozycja_zjadacza_x - promien_zjadacza) < pozycja_jedzenia_x < (pozycja_zjadacza_x + promien_zjadacza)):
        if ((pozycja_zjadacza_y - promien_zjadacza) < pozycja_jedzenia_y < (pozycja_zjadacza_y + promien_zjadacza)):
            punkty = punkty + 1
            pokaz_jedzenie()
