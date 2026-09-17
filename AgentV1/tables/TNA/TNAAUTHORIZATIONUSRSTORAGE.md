# DB2ADMIN.TNAAUTHORIZATIONUSRSTORAGE

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `TNAUNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SQN`, `TEMPLATECODE`, `LINENUMBER`, `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195585

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNAUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `HEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACTIVITYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SQN` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `LINENUMBER` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 8 | `ADDATAENTITYNAME` | CHAR(50) |  | FK | foreign_key |  |
| 9 | `ADDATANAME` | CHAR(50) |  | FK | foreign_key |  |
| 10 | `UIXMLATTRIBUTEABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 11 | `UIXMLATTRIBUTEABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 12 | `UIXMLATTRIBUTENAME` | VARCHAR(120) |  |  |  |  |
| 13 | `FIELDNAME` | VARCHAR(120) |  |  |  |  |
| 14 | `ISAD` | SMALLINT | NOT NULL |  |  |  |
| 15 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 16 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 17 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 18 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 19 | `VALUEDATE` | DATE |  |  |  |  |
| 20 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 21 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 22 | `VALUETIME` | TIME |  |  |  |  |
| 23 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_ADDATA` | `ADDATAENTITYNAME`, `ADDATANAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `TNAAUTHORIZATIONUSRSTORAGE.ADDATAENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND TNAAUTHORIZATIONUSRSTORAGE.ADDATANAME = ADADDITIONALDATA.NAME` |
| `TNAAUTHORIZEDUSER_FIELDSSTORAGE` | `TNAUNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SQN`, `TEMPLATECODE`, `LINENUMBER` | [`TNAAUTHORIZEDUSER`](../TNA/TNAAUTHORIZEDUSER.md) | `UNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SQN`, `CODE`, `LINENUMBER` | RESTRICT | `TNAAUTHORIZATIONUSRSTORAGE.TNAUNIQUEID = TNAAUTHORIZEDUSER.UNIQUEID AND TNAAUTHORIZATIONUSRSTORAGE.COMPANY = TNAAUTHORIZEDUSER.COMPANY AND TNAAUTHORIZATIONUSRSTORAGE.HEADERCODE = TNAAUTHORIZEDUSER.HEADERCODE AND TNAAUTHORIZATIONUSRSTORAGE.ACTIVITYCODE = TNAAUTHORIZEDUSER.ACTIVITYCODE AND TNAAUTHORIZATIONUSRSTORAGE.SQN = TNAAUTHORIZEDUSER.SQN AND TNAAUTHORIZATIONUSRSTORAGE.TEMPLATECODE = TNAAUTHORIZEDUSER.CODE AND TNAAUTHORIZATIONUSRSTORAGE.LINENUMBER = TNAAUTHORIZEDUSER.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TNAAUTHORIZATIONUSRSTORAGEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNAUNIQUEID,
       t.COMPANY,
       t.HEADERCODE,
       t.ACTIVITYCODE,
       t.SQN,
       t.TEMPLATECODE,
       t.LINENUMBER,
       t.UNIQUEID,
       t.ADDATAENTITYNAME,
       t.ADDATANAME,
       t.UIXMLATTRIBUTEABSUIXMLPATH,
       t.UIXMLATTRIBUTEABSUIXMLNAME
FROM   DB2ADMIN.TNAAUTHORIZATIONUSRSTORAGE t
FETCH FIRST 100 ROWS ONLY;
```
