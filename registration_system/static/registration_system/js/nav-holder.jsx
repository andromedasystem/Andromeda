import React from 'react';
import Nav from './components/container/Nav.jsx';
import { Button, Checkbox, Form, Input, Radio, Select, TextArea } from 'semantic-ui-react';
import DjangoCSRFToken from 'django-react-csrftoken';

class Index extends React.Component {

    constructor(props){
        super(props);
    }


    render() {


        return <div className="m-top8">
                <Nav
                    is_admin={this.props.is_admin}
                    is_student={this.props.is_student}/>
                <h2>{this.props.header_text}</h2>
                </div>
    }
}

export default Index;
