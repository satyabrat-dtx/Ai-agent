# DB2ADMIN.LOGEVENTMASTER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 28
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 219902

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `WSDLNAME` | VARCHAR(200) | NOT NULL |  |  |  |
| 5 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 6 | `PURCHASEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 7 | `DEBITDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 8 | `USERNAME` | CHAR(20) | NOT NULL |  |  |  |
| 9 | `PASSWORD` | CHAR(15) |  |  |  |  |
| 10 | `WSDLURL` | LONG VARCHAR | NOT NULL |  |  |  |
| 11 | `BATCHWSDLURL` | LONG VARCHAR | NOT NULL |  |  |  |
| 12 | `OPERATIONNAME` | CHAR(50) |  |  |  |  |
| 13 | `WSDLQNAMEURL` | CHAR(50) | NOT NULL |  |  |  |
| 14 | `WSDLREQUESTNAME` | CHAR(50) | NOT NULL |  |  |  |
| 15 | `WSDLREQUESTTYPE` | CHAR(50) | NOT NULL |  |  |  |
| 16 | `WSDLRESPONSENAME` | CHAR(50) | NOT NULL |  |  |  |
| 17 | `WSDLRESPONSETYPE` | CHAR(50) | NOT NULL |  |  |  |
| 18 | `SOAPACTION` | CHAR(50) | NOT NULL |  |  |  |
| 19 | `ACTIVATESERVICE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `PRODUCTIONCOST` | SMALLINT | NOT NULL |  |  |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 23 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 24 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 25 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 26 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 27 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGEVENTMASTER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.WSDLNAME,
       t.DOCUMENTTYPE,
       t.PURCHASEDOCUMENTTYPE,
       t.DEBITDOCUMENTTYPE,
       t.USERNAME,
       t.PASSWORD,
       t.WSDLURL,
       t.BATCHWSDLURL
FROM   DB2ADMIN.LOGEVENTMASTER t
FETCH FIRST 100 ROWS ONLY;
```
