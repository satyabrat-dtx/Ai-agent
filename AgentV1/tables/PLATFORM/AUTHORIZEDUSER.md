# DB2ADMIN.AUTHORIZEDUSER

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `HEADERCODE`, `TNASQN`, `COMPANY`, `CODE`, `LINENUMBER`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191470

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `HEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNASQN` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `USERIDUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 6 | `OPERATIONTYPE` | CHAR(90) |  |  |  |  |
| 7 | `ROLE` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USERID` | `USERIDUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `AUTHORIZEDUSER.USERIDUSERID = ABSUSERDEF.USERID` |
| `ACTIVITYLINKEDENTITY_AUTHORIZEDUSERS` | `COMPANY`, `HEADERCODE`, `TNASQN`, `CODE` | [`ACTIVITYLINKEDENTITY`](../TNA/ACTIVITYLINKEDENTITY.md) | `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO`, `AUTHORIZATIONTEMPLATECODE` | RESTRICT | `AUTHORIZEDUSER.COMPANY = ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCOMPANYCODE AND AUTHORIZEDUSER.HEADERCODE = ACTIVITYLINKEDENTITY.TNADETAILTNAHEADERCODE AND AUTHORIZEDUSER.TNASQN = ACTIVITYLINKEDENTITY.TNADETAILSEQNO AND AUTHORIZEDUSER.CODE = ACTIVITYLINKEDENTITY.AUTHORIZATIONTEMPLATECODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `AUTHORIZEDUSER_FIELDSSTORAGE` | [`AUTHORIZATIONUSERSTORAGE`](../PLATFORM/AUTHORIZATIONUSERSTORAGE.md) | `HEADERCODE`, `TNASQN`, `COMPANY`, `TEMPLATE_CODE`, `LINE_NUMBER` | `AUTHORIZATIONUSERSTORAGE.HEADERCODE = AUTHORIZEDUSER.HEADERCODE AND AUTHORIZATIONUSERSTORAGE.TNASQN = AUTHORIZEDUSER.TNASQN AND AUTHORIZATIONUSERSTORAGE.COMPANY = AUTHORIZEDUSER.COMPANY AND AUTHORIZATIONUSERSTORAGE.TEMPLATE_CODE = AUTHORIZEDUSER.CODE AND AUTHORIZATIONUSERSTORAGE.LINE_NUMBER = AUTHORIZEDUSER.LINENUMBER` |

## Indexes

- `AUTHORIZEDUSERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.HEADERCODE,
       t.TNASQN,
       t.COMPANY,
       t.CODE,
       t.LINENUMBER,
       t.USERIDUSERID,
       t.OPERATIONTYPE,
       t.ROLE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.AUTHORIZEDUSER t
FETCH FIRST 100 ROWS ONLY;
```
