# DB2ADMIN.ADSTORAGE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `UNIQUEID`, `NAMEENTITYNAME`, `NAMENAME`, `FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61196

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key | Unique id of the linked record |
| 1 | `NAMEENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key | Entity Table name  |
| 2 | `NAMENAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `KEYSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SHARED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DATATYPE` | INTEGER | NOT NULL |  |  | Stores integer value based on datatype, 0-sting, 1-Integer,2-Boolean,3-Date,4-Decimal,5-Long,6-Time,7-Timestamp. Based on value, right value from column 7-14 is fetched.  |
| 7 | `VALUESTRING` | VARCHAR(250) |  |  |  |  |
| 8 | `VALUEINT` | INTEGER | NOT NULL |  |  |  |
| 9 | `VALUEBOOLEAN` | SMALLINT | NOT NULL |  |  |  |
| 10 | `VALUEDATE` | DATE |  |  |  |  |
| 11 | `VALUEDECIMAL` | DECIMAL(18,5) |  |  |  |  |
| 12 | `VALUELONG` | BIGINT | NOT NULL |  |  |  |
| 13 | `VALUETIME` | TIME |  |  |  |  |
| 14 | `VALUETIMESTAMP` | TIMESTAMP |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADADDITIONALDATA_NAME` | `NAMEENTITYNAME`, `NAMENAME` | [`ADADDITIONALDATA`](../CORE_MASTER/ADADDITIONALDATA.md) | `ENTITYNAME`, `NAME` | RESTRICT | `ADSTORAGE.NAMEENTITYNAME = ADADDITIONALDATA.ENTITYNAME AND ADSTORAGE.NAMENAME = ADADDITIONALDATA.NAME` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADSTORAGE1` (FIELDNAME, NAMEENTITYNAME)
- `ADSTORAGEUID` (ABSUNIQUEID)
- `ADSTORAGEIDX1` (NAMEENTITYNAME, FIELDNAME, UNIQUEID, VALUESTRING)
- `ADSTORAGEIDX2` (NAMEENTITYNAME, FIELDNAME, UNIQUEID, VALUEDECIMAL)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.NAMEENTITYNAME,
       t.NAMENAME,
       t.FIELDNAME,
       t.KEYSEQUENCE,
       t.SHARED,
       t.DATATYPE,
       t.VALUESTRING,
       t.VALUEINT,
       t.VALUEBOOLEAN,
       t.VALUEDATE,
       t.VALUEDECIMAL
FROM   DB2ADMIN.ADSTORAGE t
FETCH FIRST 100 ROWS ONLY;
```
