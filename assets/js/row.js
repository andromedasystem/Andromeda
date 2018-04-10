import React from 'react';
import { Container, Divider, Header, Table, List, Segment, Dimmer, Loader } from 'semantic-ui-react';
import Modal from 'react-responsive-modal';

class ScheduleRow extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            data: this.props.data,
            isShowingModal: false
        };
        this.handleClick = this.handleClick.bind(this);
        this.handleClose = this.handleClose.bind(this);
    }

    handleClick(event){
		this.setState({
			isShowingModal: true
		});
	}

    handleClose(){
		this.setState({
			isShowingModal: false
		});
	}

    render(){
        const prereqs = this.state.data.prerequisites.map((item, i) => {
                return <List.Item>
                            <List.Content>
                                <List.Description as='h5'>{item.name}</List.Description>
                            </List.Content>
                       </List.Item>
            });
        return(
        <Table.Row onClick={this.handleClick}>
            <Table.Cell>
                <Header as='h2' textAlign='center'>{this.state.data.section_id}</Header>
            </Table.Cell>
            <Table.Cell singleLine>
                <Header as='h4' textAlign='center'>{this.state.data.course_name}</Header>
            </Table.Cell>
            <Table.Cell singleLine>{this.state.data.faculty}</Table.Cell>
            <Table.Cell>{this.state.data.credits}</Table.Cell>
            <Table.Cell textAlign='left'>
                <strong>Seats Taken: </strong>{this.state.data.seats_taken}<br />
                <strong>Seating Capacity: </strong>{this.state.data.capacity}
            </Table.Cell>
            <Table.Cell textAlign='center'>
                <strong>{this.state.data.meeting_days}</strong><br/>
                {this.state.data.time_period}
            </Table.Cell>
            <Table.Cell textAlign='center'>
                <strong>Building: </strong>{this.state.data.building}<br/>
                <strong>Room: </strong>{this.state.data.room}
            </Table.Cell>
            <Table.Cell textAlign='center'>
                <List divided relaxed>
                    {prereqs}
                </List>
            </Table.Cell>
            <Modal open={this.state.isShowingModal} onClose={this.handleClose} >
				<h1>{this.state.data.course_name}</h1>
				<h4>Course Description</h4>
                <p>{this.state.data.course_description}</p>
                <h4>Credits</h4>
                <p>{this.state.data.credits}</p>
                <h4>Prerequisites</h4>
                {prereqs}
			</Modal>
       </Table.Row>
        );

    }
}

export default ScheduleRow;