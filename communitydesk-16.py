# === Stage 16: Add argparse support for the most common commands ===
# Project: CommunityDesk
import argparse

def main():
    parser = argparse.ArgumentParser(description="CommunityDesk CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Members command
    members_parser = subparsers.add_parser('members', help='Manage members')
    members_parser.add_argument('-l', '--list', action='store_true', help='List all members')
    members_parser.add_argument('-a', '--add', type=str, help='Add a new member (name,email)')
    
    # Requests command
    requests_parser = subparsers.add_parser('requests', help='Manage requests')
    requests_parser.add_argument('-l', '--list', action='store_true', help='List all requests')
    requests_parser.add_argument('-c', '--close', type=int, help='Close request by ID')
    
    # Events command
    events_parser = subparsers.add_parser('events', help='Manage events')
    events_parser.add_argument('-l', '--list', action='store_true', help='List all events')
    events_parser.add_argument('-c', '--create', type=str, help='Create event (title,date)')
    
    # Volunteers command
    volunteers_parser = subparsers.add_parser('volunteers', help='Manage volunteers')
    volunteers_parser.add_argument('-l', '--list', action='store_true', help='List all volunteers')
    volunteers_parser.add_argument('-a', '--add', type=str, help='Add a new volunteer (name,skills)')
    
    # Announcements command
    announcements_parser = subparsers.add_parser('announcements', help='Manage announcements')
    announcements_parser.add_argument('-l', '--list', action='store_true', help='List all announcements')
    announcements_parser.add_argument('-c', '--create', type=str, help='Create announcement (title,message)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Placeholder logic for command execution
    print(f"Executing command: {args.command}")
    if hasattr(args, 'list'):
        print("Listing items...")
    elif hasattr(args, 'add') or hasattr(args, 'create'):
        print(f"Adding item: {getattr(args, 'add', '')} / {getattr(args, 'create', '')}")
    elif hasattr(args, 'close'):
        print(f"Closing request ID: {args.close}")

if __name__ == '__main__':
    main()
