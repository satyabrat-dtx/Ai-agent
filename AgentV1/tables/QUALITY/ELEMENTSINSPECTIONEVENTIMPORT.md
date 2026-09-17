# DB2ADMIN.ELEMENTSINSPECTIONEVENTIMPORT

- **Module**: `QUALITY` (low confidence — table name starts with 'ELEMENT')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `ELEMENTSINSIMPORTCOMPANYCODE`, `ELEMENTSINSIMPORTITEMTYPECODE`, `ELEMENTSINSIMPORTEVENTSLINK`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 75475

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ELEMENTSINSIMPORTCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `ELEMENTSINSIMPORTITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ELEMENTSINSIMPORTEVENTSLINK` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 4 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `CODEEVENTCODE` | CHAR(3) |  |  |  |  |
| 6 | `STARTPOSITION` | DECIMAL(7,2) | NOT NULL |  |  |  |
| 7 | `LENGHT` | DECIMAL(7,2) |  |  |  |  |
| 8 | `WIDTHPOSITION` | DECIMAL(7,2) |  |  |  |  |
| 9 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 10 | `ZONE` | CHAR(4) |  |  |  |  |
| 11 | `POINTS` | DECIMAL(5,2) |  |  |  |  |
| 12 | `CREDITS` | DECIMAL(7,2) |  |  |  |  |
| 13 | `EVENTVALUE` | VARCHAR(100) |  |  |  |  |
| 14 | `VARIABLE` | VARCHAR(250) |  |  |  |  |
| 15 | `STARTDATETIME` | TIMESTAMP |  |  |  |  |
| 16 | `ENDDATETIME` | TIMESTAMP |  |  |  |  |
| 17 | `CALCULATED` | SMALLINT | NOT NULL |  |  |  |
| 18 | `SPLICE` | SMALLINT | NOT NULL |  |  |  |
| 19 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ELEMENTSINSEVENTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ELEMENTSINSIMPORTCOMPANYCODE,
       t.ELEMENTSINSIMPORTITEMTYPECODE,
       t.ELEMENTSINSIMPORTEVENTSLINK,
       t.IMPORTSTATUS,
       t.SEQUENCE,
       t.CODEEVENTCODE,
       t.STARTPOSITION,
       t.LENGHT,
       t.WIDTHPOSITION,
       t.WIDTH,
       t.ZONE,
       t.POINTS
FROM   DB2ADMIN.ELEMENTSINSPECTIONEVENTIMPORT t
FETCH FIRST 100 ROWS ONLY;
```
