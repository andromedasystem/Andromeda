import React from 'react';
import { Container, Divider, Header, Table, Form, Segment, Dimmer, Loader } from 'semantic-ui-react';
import MasterTable from './table';


class App extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            isLoading: true,
        };
        this.onBlur = this.onBlur.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSelectChange = this.handleSelectChange.bind(this);
    }

    componentDidMount(){
        fetch("/student_system/student_system_api/get_general_data/")
            .then((response) => {
                if(!response.ok){
                    throw Error(response.statusText);
                }

                return response;
            })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                let department_options = [];
                let time_period_options = [];
                let meeting_day_options = [];
                let building_options = [];
                let room_options = [];
                let faculty_options = [];
                let d, f, b, t, m, r;
                for( let d of data.departments){
                   let department_data = {
                        key:  d.department_id,
                        text: d.department_name,
                        value: d.department_id,
                    };
                    department_options.push(department_data);
                }
                for( let t of data.time_periods){
                   let time_period_data = {
                        key:  t.time_period_id,
                        text: t.time_range,
                        value: t.time_period_id,
                    };
                    time_period_options.push(time_period_data);
                }
                for( let m of data.meeting_days){
                   let meeting_day_data = {
                        key:  m.days_id,
                        text: m.day_range,
                        value: m.days_id,
                    };
                    meeting_day_options.push(meeting_day_data);
                }
                for( let b of data.buildings){

                   let buildings_data = {
                        key:  b.building_id,
                        text: b.building_name,
                        value: b.building_id,
                    };
                   building_options.push(buildings_data);
                }
                for( let r of data.rooms){
                   let room_data = {
                        key:  r.rooms_id,
                        text: r.room_number,
                        value: r.rooms_id,
                    };
                   room_options.push(room_data);
                }
                for( let f of data.faculty){
                   let faculty_data = {
                        key:  f.faculty_id,
                        text: f.full_name,
                        value: f.faculty_id,
                    };
                   faculty_options.push(faculty_data);
                }


                this.setState({
                    departments: department_options,
                    time_periods: time_period_options,
                    meeting_days: meeting_day_options,
                    building: building_options,
                    rooms: room_options,
                    faculty: faculty_options,
                    isLoading: false
                });
            })
            .catch((error) => {
                console.error(error);
            })
    }

    handleInputChange(event) {
        this.setState({
            [event.target.id]: event.target.value
        })
    }

    onBlur(){
        this.setState({
            submittedValue: this.state.course_name_input,
            attributeFlag: 'course_name'
        })
    }

    handleSelectChange(value, id){
        console.log(value);
        console.log(id);
        let attribute_flag;
        switch(id){
            case 'department_select':
                attribute_flag = 'department';
                break;
            case 'faculty_select':
                attribute_flag = 'faculty';
                break;
            case 'days_select':
                attribute_flag = 'days';
                break;
            case 'time_period_select':
                attribute_flag = 'time_period';
                break;
            case 'building_select':
                attribute_flag = 'building';
                break;
            case 'room_select':
                attribute_flag = 'rooms';
                break;
        }
        console.log(value);
        this.setState({
            submittedValue: value,
            attributeFlag: attribute_flag
        });
    }

    render() {

        if( this.state.isLoading){
            return(
                <Segment>
                  <Dimmer active>
                    <Loader size='massive'>Loading</Loader>
                  </Dimmer>
                </Segment>
            );
        }
        return (
            <Container >
                <Form>
                    <Form.Group widths='equal'>
                        <Form.Select id='department_select' onChange={(e, {value, id}) => this.handleSelectChange(value, id)} fluid label='Department Name'  options={this.state.departments} placeholder='Department Name'/>
                        <Form.Input id='course_name_input' onBlur={this.onBlur} onChange={this.handleInputChange} fluid label='Course Name' placeholder='Course Name'/>
                    </Form.Group>
                    <Form.Select id='faculty_select' onChange={(e, {value, id}) => this.handleSelectChange(value, id)} fluid label='Faculty' options={this.state.faculty} placeholder='Faculty'/>
                    <Form.Group widths='equal'>
                        <Form.Select id='days_select' onChange={(e, {value, id}) => this.handleSelectChange(value, id)} fluid label='Meeting Days' options={this.state.meeting_days} placeholder='Meeting Days'/>
                        <Form.Select id='time_period_select' onChange={(e, {value, id}) => this.handleSelectChange(value, id)} fluid label='Time Periods' options={this.state.time_periods} placeholder='Time Periods'/>
                    </Form.Group>
                    <Form.Group widths='equal'>
                        <Form.Select id='building_select' onChange={(e, {value, id}) => this.handleSelectChange(value, id)} fluid label='Buldings' options={this.state.building} placeholder='Buildings'/>
                        <Form.Select id='room_select' onChange={(e, {value, id}) => this.handleSelectChange(value, id)} fluid label='Rooms' options={this.state.rooms} placeholder='Rooms'/>
                    </Form.Group>

                </Form>
                <Divider horizontal>Results</Divider>
                { (this.state.submittedValue) &&
                    <MasterTable search_value={this.state.submittedValue} attribute_flag={this.state.attributeFlag} />
                }
            </Container>
        );
    }

}



export default App;