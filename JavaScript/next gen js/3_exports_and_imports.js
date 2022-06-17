// Imaginar un archivo person.js

const person = {
    name: 'Max'
}

export default person


//-----------------------------------------------------------------------------------------------

// Imaginar un archivo utility.js

export const clean = () => {...}

export const baseData = 10;



//-----------------------------------------------------------------------------------------------
// Archivo local app.js

import person from './person.js'
import prs from './person.js'

// Estas dos imports seran iguales sin importar el nombre gracias al uso del default keyword


import {baseData} from './utility.js'
import {clean as cln} from './utility.js' // se puede asignar un alias

// Como son dos imports, se debe especificar el nombre exacto entre {}


import * as alias from './utility.js' // se importara todo el contenido exportado de utility.js como un objeto llamado alias
// ej: alias.baseData
