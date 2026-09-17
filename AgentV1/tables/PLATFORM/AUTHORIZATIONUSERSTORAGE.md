# DB2ADMIN.AUTHORIZATIONUSERSTORAGE

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `HEADERCODE`, `TNASQN`, `COMPANY`, `TEMPLATE_CODE`, `LINE_NUMBER`, `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191413

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `HEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNASQN` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TEMPLATE_CODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINE_NUMBER` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `ADDATAENTITYNAME` | CHAR(50) |  | FK | foreign_key |  |
| 7 | `ADDATANAME` | CHAR(50) |  | FK | foreign_key |  |
| 8 | `UIXMLATTRIBUTEABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 9 | `UIXMLATTRIBUTEABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 10 | `UIXMLATTRIBUTENAME` | VARCHAR(120) |  |  |  |  |
| 11 | `FIELDNAME` | VARCHAR(120) |  |  |  |  |
| 12 | `ISAD` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 14 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 15 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 16 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 17 | `VALUEDATE` | DATE |  |  |  |  |
| 18 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 19 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 20 | `VALUETIME` | TIME |  |  |  |  |
| 21 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_ADDATA` | `ADDATAENTITYNAME`, `ADDATANAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `AUTHORIZATIONUSERSTORAGE.ADDATAENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND AUTHORIZATIONUSERSTORAGE.ADDATANAME = ADADDITIONALDATA.NAME` |
| `AUTHORIZEDUSER_FIELDSSTORAGE` | `HEADERCODE`, `TNASQN`, `COMPANY`, `TEMPLATE_CODE`, `LINE_NUMBER` | [`AUTHORIZEDUSER`](../PLATFORM/AUTHORIZEDUSER.md) | `HEADERCODE`, `TNASQN`, `COMPANY`, `CODE`, `LINENUMBER` | RESTRICT | `AUTHORIZATIONUSERSTORAGE.HEADERCODE = AUTHORIZEDUSER.HEADERCODE AND AUTHORIZATIONUSERSTORAGE.TNASQN = AUTHORIZEDUSER.TNASQN AND AUTHORIZATIONUSERSTORAGE.COMPANY = AUTHORIZEDUSER.COMPANY AND AUTHORIZATIONUSERSTORAGE.TEMPLATE_CODE = AUTHORIZEDUSER.CODE AND AUTHORIZATIONUSERSTORAGE.LINE_NUMBER = AUTHORIZEDUSER.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `AUTHORIZATIONUSERSTORAGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.HEADERCODE,
       t.TNASQN,
       t.COMPANY,
       t.TEMPLATE_CODE,
       t.LINE_NUMBER,
       t.UNIQUEID,
       t.ADDATAENTITYNAME,
       t.ADDATANAME,
       t.UIXMLATTRIBUTEABSUIXMLPATH,
       t.UIXMLATTRIBUTEABSUIXMLNAME,
       t.UIXMLATTRIBUTENAME,
       t.FIELDNAME
FROM   DB2ADMIN.AUTHORIZATIONUSERSTORAGE t
FETCH FIRST 100 ROWS ONLY;
```
