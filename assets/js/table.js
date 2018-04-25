import React from 'react';
import { Container, Divider, Header, Table, List, Segment, Dimmer, Loader } from 'semantic-ui-react';
import ScheduleRow from './row';


// TODO: Create table and implement data fetching
class MasterTable extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            attribute_flag: this.props.attribute_flag,
            isLoading: true,
            search_value: this.props.search_value,
            semester_id: this.props.semester_id,
            department_id: this.props.department_id,
            faculty_id: this.props.faculty_id,
            days_id: this.props.days_id,
            period_id: this.props.period_id,
            building_id: this.props.building_id,
            room_id: this.props.room_id,
            course_name: this.props.course_name
        };
        // this.onBlur = this.onBlur.bind(this);
        // this.handleInputChange = this.handleInputChange.bind(this);
        // this.handleSelectChange = this.handleSelectChange.bind(this);
    }

    componentDidMount(){
         const postData = {
             method: 'POST',
             headers: {
                 'Content-Type': 'application/json',
                 'Accept': 'application/json'
             },
             body: JSON.stringify({
                semester_id: this.state.semester_id,
                department_id: this.state.department_id,
                faculty_id: this.state.faculty_id,
                days_id: this.state.days_id,
                building_id: this.state.building_id,
                period_id: this.state.period_id,
                room_id: this.state.room_id,
                course_name: this.state.course_name
             })
         };

         //fetch("/student_system/student_system_api/get_schedule_data/"+ this.state.attribute_flag +"/" + this.state.search_value +"/")
         fetch("/student_system/student_system_api/get_schedule_data/v2/", postData)
            .then((response) => {
                if(!response.ok){
                    throw Error(response.statusText);
                }

                return response;
            })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                this.setState({
                    isLoading: false,
                    table_data: data
                })
            })
            .catch((error) => {
                console.error(error);
            })
    }

    componentWillReceiveProps(nextProps){
        if(this.props.semester_id !== nextProps.semester_id || this.props.department_id !== nextProps.department_id
            || this.props.faculty_id !== nextProps.faculty_id || this.props.days_id !== nextProps.days_id
            || this.props.period_id !== nextProps.period_id || this.props.building_id !== nextProps.building_id
            || this.props.room_id !== nextProps.room_id || this.props.course_name !== nextProps.course_name) {
            const postData = {
                 method: 'POST',
                 headers: {
                     'Content-Type': 'application/json',
                     'Accept': 'application/json'
                 },
                 body: JSON.stringify({
                    semester_id: nextProps.semester_id,
                    department_id: nextProps.department_id,
                    faculty_id: nextProps.faculty_id,
                    days_id:  nextProps.days_id,
                    building_id: nextProps.building_id,
                    period_id: nextProps.period_id,
                    room_id: nextProps.room_id,
                    course_name: nextProps.course_name
                 })
             };
             //fetch("/student_system/student_system_api/get_schedule_data/"+ nextProps.attribute_flag +"/" + nextProps.search_value +"/")
            fetch("/student_system/student_system_api/get_schedule_data/v2/", postData)
            .then((response) => {
                if(!response.ok){
                    throw Error(response.statusText);
                }
                return response;
            })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                this.setState({
                    isLoading: false,
                    table_data: data
                })
            })
            .catch((error) => {
                console.error(error);
            })
        }

    }

    render() {
         if( this.state.isLoading){
            return(
                <div style={{height: '100%'}}><Segment >
                  <Dimmer active>
                    <Loader size='massive'>Loading</Loader>
                  </Dimmer>
                </Segment></div>
            );
        }
        let rows;
        if( this.state.table_data){
            rows = this.state.table_data.map((item, i) => {
                return <ScheduleRow
                        key={ i }
                        data={ item }
                        // onClick={() => this.handleClick(item.section_id)}
                        />
            })
        }

        return(
            <div>
                <Table color={'black'} celled selectable padded>
                    <Table.Header >
                        <Table.Row>
                            <Table.HeaderCell singleLine>Section</Table.HeaderCell>
                            <Table.HeaderCell>Course Name</Table.HeaderCell>
                            <Table.HeaderCell>Professor</Table.HeaderCell>
                            <Table.HeaderCell>Credits</Table.HeaderCell>
                            <Table.HeaderCell width={3}>Seating</Table.HeaderCell>
                            <Table.HeaderCell>Time Slot</Table.HeaderCell>
                            <Table.HeaderCell>Semester</Table.HeaderCell>
                            <Table.HeaderCell width={2}>Location</Table.HeaderCell>
                            <Table.HeaderCell>Prerequisites</Table.HeaderCell>
                        </Table.Row>
                    </Table.Header>

                    <Table.Body>
                        {rows}
                    </Table.Body>
                </Table>
            </div>
        )

    }

}


export default MasterTable;
