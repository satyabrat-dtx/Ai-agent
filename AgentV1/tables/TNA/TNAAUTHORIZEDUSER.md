# DB2ADMIN.TNAAUTHORIZEDUSER

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `UNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SQN`, `CODE`, `LINENUMBER`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195646

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `HEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACTIVITYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SQN` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `USERIDUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 8 | `OPERATIONTYPE` | CHAR(90) |  |  |  |  |
| 9 | `ROLE` | INTEGER | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USERID` | `USERIDUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `TNAAUTHORIZEDUSER.USERIDUSERID = ABSUSERDEF.USERID` |
| `TNAACTIVITYLINKEDENTITY_AUTHORIZEDUSERS` | `UNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SQN`, `CODE` | [`TNAACTIVITYLINKEDENTITY`](../TNA/TNAACTIVITYLINKEDENTITY.md) | `UNIQUEID`, `COMPANY`, `TNAHEADERCODE`, `ACTIVITYCODE`, `SEQNO`, `AUTHORIZATIONTEMPLATECODE` | RESTRICT | `TNAAUTHORIZEDUSER.UNIQUEID = TNAACTIVITYLINKEDENTITY.UNIQUEID AND TNAAUTHORIZEDUSER.COMPANY = TNAACTIVITYLINKEDENTITY.COMPANY AND TNAAUTHORIZEDUSER.HEADERCODE = TNAACTIVITYLINKEDENTITY.TNAHEADERCODE AND TNAAUTHORIZEDUSER.ACTIVITYCODE = TNAACTIVITYLINKEDENTITY.ACTIVITYCODE AND TNAAUTHORIZEDUSER.SQN = TNAACTIVITYLINKEDENTITY.SEQNO AND TNAAUTHORIZEDUSER.CODE = TNAACTIVITYLINKEDENTITY.AUTHORIZATIONTEMPLATECODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TNAAUTHORIZEDUSER_FIELDSSTORAGE` | [`TNAAUTHORIZATIONUSRSTORAGE`](../TNA/TNAAUTHORIZATIONUSRSTORAGE.md) | `TNAUNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SQN`, `TEMPLATECODE`, `LINENUMBER` | `TNAAUTHORIZATIONUSRSTORAGE.TNAUNIQUEID = TNAAUTHORIZEDUSER.UNIQUEID AND TNAAUTHORIZATIONUSRSTORAGE.COMPANY = TNAAUTHORIZEDUSER.COMPANY AND TNAAUTHORIZATIONUSRSTORAGE.HEADERCODE = TNAAUTHORIZEDUSER.HEADERCODE AND TNAAUTHORIZATIONUSRSTORAGE.ACTIVITYCODE = TNAAUTHORIZEDUSER.ACTIVITYCODE AND TNAAUTHORIZATIONUSRSTORAGE.SQN = TNAAUTHORIZEDUSER.SQN AND TNAAUTHORIZATIONUSRSTORAGE.TEMPLATECODE = TNAAUTHORIZEDUSER.CODE AND TNAAUTHORIZATIONUSRSTORAGE.LINENUMBER = TNAAUTHORIZEDUSER.LINENUMBER` |

## Indexes

- `TNAAUTHORIZEDUSERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANY,
       t.HEADERCODE,
       t.ACTIVITYCODE,
       t.SQN,
       t.CODE,
       t.LINENUMBER,
       t.USERIDUSERID,
       t.OPERATIONTYPE,
       t.ROLE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.TNAAUTHORIZEDUSER t
FETCH FIRST 100 ROWS ONLY;
```
