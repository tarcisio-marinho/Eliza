#!/bin/bash
musica=$(zenity --file-selection --title="Selecione a musica");
amarok $musica
