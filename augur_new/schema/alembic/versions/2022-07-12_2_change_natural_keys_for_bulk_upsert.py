"""Change natural keys for bulk upsert

Revision ID: 2
Revises: 1
Create Date: 2022-07-12 10:21:03.009319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2'
down_revision = '1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # create issue assignee unique for inserts
    op.create_unique_constraint('issue-assignee-insert-unique', 'issue_assignees', ['issue_assignee_src_id', 'issue_id'], schema='augur_data')

    # update issue message ref unique for inserts
    op.drop_constraint('repo-issue', 'issue_message_ref', schema='augur_data', type_='unique')
    op.create_unique_constraint('issue-message-ref-insert-unique', 'issue_message_ref', ['issue_msg_ref_src_comment_id', 'issue_id'], schema='augur_data')

    # create issue unique for inserts
    op.create_unique_constraint('issue-insert-unique', 'issues', ['issue_url'], schema='augur_data')

    # update message unique for inserts
    op.drop_constraint('gh-message', 'message', schema='augur_data', type_='unique')
    op.create_unique_constraint('message-insert-unique', 'message', ['platform_msg_id'], schema='augur_data')

    # update pull request message ref unique for inserts
    op.drop_constraint('pr-comment-nk', 'pull_request_message_ref', schema='augur_data', type_='unique')
    op.create_unique_constraint('pull-request-message-ref-insert-unique', 'pull_request_message_ref', ['pr_message_ref_src_comment_id', 'pull_request_id'], schema='augur_data')

    # create pull request meta unique for inserts
    op.create_unique_constraint('pull-request-meta-insert-unique', 'pull_request_meta', ['pull_request_id', 'pr_head_or_base', 'pr_sha'], schema='augur_data')

    # update pull request review message ref unique for inserts
    op.drop_constraint('pr-review-nk', 'pull_request_review_message_ref', schema='augur_data', type_='unique')
    op.create_unique_constraint('pull-request-review-message-ref-insert-unique', 'pull_request_review_message_ref', ['pr_review_msg_src_id'], schema='augur_data')

    # create pull request unique for inserts
    op.create_unique_constraint('pull-request-insert-unique', 'pull_requests', ['pr_url'], schema='augur_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pull-request-insert-unique', 'pull_requests', schema='augur_data', type_='unique')
    op.drop_constraint('pull-request-review-message-ref-insert-unique', 'pull_request_review_message_ref', schema='augur_data', type_='unique')
    op.create_unique_constraint('pr-review-nk', 'pull_request_review_message_ref', ['pr_review_msg_src_id', 'tool_source'], schema='augur_data')
    op.drop_constraint('pull-request-meta-insert-unique', 'pull_request_meta', schema='augur_data', type_='unique')
    op.drop_constraint('pull-request-message-ref-insert-unique', 'pull_request_message_ref', schema='augur_data', type_='unique')
    op.create_unique_constraint('pr-comment-nk', 'pull_request_message_ref', ['pr_message_ref_src_comment_id', 'tool_source'], schema='augur_data')
    op.drop_constraint('message-insert-unique', 'message', schema='augur_data', type_='unique')
    op.create_unique_constraint('gh-message', 'message', ['platform_msg_id', 'tool_source'], schema='augur_data')
    op.drop_constraint('issue-insert-unique', 'issues', schema='augur_data', type_='unique')
    op.drop_constraint('issue-message-ref-insert-unique', 'issue_message_ref', schema='augur_data', type_='unique')
    op.create_unique_constraint('repo-issue', 'issue_message_ref', ['issue_msg_ref_src_comment_id', 'tool_source'], schema='augur_data')
    op.drop_constraint('issue-assignee-insert-unique', 'issue_assignees', schema='augur_data', type_='unique')
    # ### end Alembic commands ###
