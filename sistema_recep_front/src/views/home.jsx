import React, { useState, useEffect,useCallback,useRef } from 'react';
import LogoHomeRodape from './assets/images/LogoHomeRodape.svg';

import './assets/styles/home.css'; // Importe o arquivo CSS para aplicar estilos
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faCaretDown, faCogs, faUserTie, faHeadset, faKey, faSignOutAlt, faCalendarAlt, faMapMarkerAlt, faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';
import axios from 'axios';  // Não esqueça de importar o axios, pois está usando ele no código.



const Home = () => {
   

        

    return (
        <div className="home-container">
            <div className="left-container">
                <div className="left-card">
                    <h2 className='left-home-text'>Cadastro de novo visitante</h2>
                    <p className='left-home-subtext'>Digite as suas credenciais nos campos abaixo</p>
                    <div className="input-container-home">
                        <label htmlFor="name">Nome</label>
                        <input className='inputHome' type="text" id="name" placeholder="Nome" />
                    </div>
                    <div className="input-container-home">
                        <label htmlFor="phone">Telefone</label>
                        <input className='inputHome' type="text" id="phone" placeholder="Telefone" />
                    </div>

                    <div className="input-container-home">
                        <label htmlFor="cpf">CPF</label>
                        <input className='inputHome' type="text" id="cpf" placeholder="CPF" />
                    </div>
                    <div className="input-container-home">
                        <label htmlFor="office">Gabinete</label>
                        <select id="office" className="inputHome">
                            <option value="office1">Gabinete 1</option>
                            <option value="office2">Gabinete 2</option>
                            {/* Adicione mais opções conforme necessário */}
                        </select>
                    </div>

                    <button className="register-button">Cadastrar</button>
                </div>
            </div>
            <div className="right-container">
             <div className="right-card"></div>
           
            </div>
            <div className="footer">
                <img className="logo" src={LogoHomeRodape} alt="Logo" />
            </div>
        </div>
    );



};



function HomeScreen() {





    return (


            
        <div>
            <Home/>

            </div>


        
    );
}

export default HomeScreen;
