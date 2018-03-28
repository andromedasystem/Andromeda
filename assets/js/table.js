import React from 'react';
import { Container, Divider, Header, Table, Form } from 'semantic-ui-react';

// TODO: Create table and implement data fetching
class MasterTable extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            attribute_flag: this.props.attribute_flag,
            isLoading: false,
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

            })
            .catch((error) => {
                console.error(error);
            })
        }

    }


    render() {
        return(
            <div>
                hello world
            </div>
        )

    }

}

export default MasterTable;
