# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: CommunityDesk
import sys, signal


def handle_interrupt(signum, frame):
    print("\nCommunityDesk: interrupt received. Exiting gracefully...")
    try:
        # Close any open files or connections before exiting
        for attr in (
            'open_files', 'sockets', 'connections'
        ):
            obj = getattr(sys.modules.get('communitydesk', None), attr, None)
            if hasattr(obj, '__iter__'):
                for item in list(obj):
                    try:
                        item.close()
                    except Exception:
                        pass
    except Exception:
        pass

    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)
