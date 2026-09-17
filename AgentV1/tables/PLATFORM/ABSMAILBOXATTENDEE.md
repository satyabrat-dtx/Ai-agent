# DB2ADMIN.ABSMAILBOXATTENDEE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ABSMAILBOXMAILIDENTIFIER`, `ADDRESSTYPE`, `ATTENDEE`, `ATTENDEEINTERNALUSERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117760

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSMAILBOXMAILIDENTIFIER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ATTENDEETYPE` | INTEGER | NOT NULL |  |  |  |
| 2 | `ADDRESSTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ATTENDEE` | CHAR(150) | NOT NULL | PK | primary_key |  |
| 4 | `ATTENDEEINTERNALUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 5 | `ATTENDEESTATUS` | INTEGER | NOT NULL |  |  |  |
| 6 | `VALIDSENTADDRESS` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSMAILBOX_ATTENDEES` | `ABSMAILBOXMAILIDENTIFIER` | [`ABSMAILBOX`](../PLATFORM/ABSMAILBOX.md) | `MAILIDENTIFIER` | RESTRICT | `ABSMAILBOXATTENDEE.ABSMAILBOXMAILIDENTIFIER = ABSMAILBOX.MAILIDENTIFIER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSMAILBOXATTENDEEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSMAILBOXMAILIDENTIFIER,
       t.ATTENDEETYPE,
       t.ADDRESSTYPE,
       t.ATTENDEE,
       t.ATTENDEEINTERNALUSERID,
       t.ATTENDEESTATUS,
       t.VALIDSENTADDRESS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSMAILBOXATTENDEE t
FETCH FIRST 100 ROWS ONLY;
```
