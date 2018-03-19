import React from 'react';
import Nav from './components/container/Nav.jsx';
import { Button, Checkbox, Form, Input, Radio, Select, TextArea } from 'semantic-ui-react';

class Index extends React.Component {

    constructor(props){
        super(props);
    }

    render() {
        let departments = this.props.departments.map((department, index) => {
            return <option key={department.value} value={department.value}>{department.name}</option>
        });

        return <div className="m-top8">
                <Nav
                    is_admin={this.props.is_admin}/>
                <h2>Create Course</h2>
                <Form action={this.props.url} method="post" className="m-top2">
                    <Form.Group widths='equal'>
                        <Form.Input required fluid label='Name' name='name' maxLength="100" placeholder="Enter Course Name" id='id_name'/>
                        <Form.Input required fluid label='Credits' name='credits' type='number' step={1} min={2} max={4} id="id_credits"/>
                    </Form.Group>
                    <Form.TextArea label="Description" placeholder="Enter Course Description..." name='description' maxLength={1000} required id="id_description"/>
                    <Form.Group inline>
                        <Form.Field  required label="Department" control='select' name="department_id" id="id_department_id">
                            <option key="0" value>---------</option>
                            {departments}
                        </Form.Field>
                    </Form.Group>
                    <Form.Button>Submit</Form.Button>
                </Form>
            </div>
    }
}

export default Index;
