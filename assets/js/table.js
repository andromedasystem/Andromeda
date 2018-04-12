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
            search_value: this.props.search_value
        };
        // this.onBlur = this.onBlur.bind(this);
        // this.handleInputChange = this.handleInputChange.bind(this);
        // this.handleSelectChange = this.handleSelectChange.bind(this);
    }

    componentDidMount(){
         fetch("/student_system/student_system_api/get_schedule_data/"+ this.state.attribute_flag +"/" + this.state.search_value +"/")
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
        if(this.props.search_value !== nextProps.search_value){
             fetch("/student_system/student_system_api/get_schedule_data/"+ nextProps.attribute_flag +"/" + nextProps.search_value +"/")
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
