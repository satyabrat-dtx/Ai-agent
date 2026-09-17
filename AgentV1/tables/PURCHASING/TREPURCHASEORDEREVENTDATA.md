# DB2ADMIN.TREPURCHASEORDEREVENTDATA

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `EVENTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69378

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EVENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `EVENTDATE` | DATE |  |  |  |  |
| 5 | `EVENTTIME` | TIME |  |  |  |  |
| 6 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 7 | `EVENTNOTE` | VARCHAR(100) |  |  |  |  |
| 8 | `EVENTREFERENCE` | VARCHAR(100) |  |  |  |  |
| 9 | `EVENTCOMMENT` | VARCHAR(3000) |  |  |  |  |
| 10 | `EVENTENTRYTYPE` | CHAR(1) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDER_PURCHASEORDER` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `TREPURCHASEORDEREVENTDATA.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND TREPURCHASEORDEREVENTDATA.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND TREPURCHASEORDEREVENTDATA.PURCHASEORDERCODE = PURCHASEORDER.CODE` |
| `TREPURCHASEORDEREVENT_EVENT` | `PURCHASEORDERCOMPANYCODE`, `EVENTCODE` | [`TREPURCHASEORDEREVENT`](../PURCHASING/TREPURCHASEORDEREVENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREPURCHASEORDEREVENTDATA.PURCHASEORDERCOMPANYCODE = TREPURCHASEORDEREVENT.COMPANYCODE AND TREPURCHASEORDEREVENTDATA.EVENTCODE = TREPURCHASEORDEREVENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREPURCHASEORDEREVENTDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.EVENTCODE,
       t.EVENTDATE,
       t.EVENTTIME,
       t.SEQUENCE,
       t.EVENTNOTE,
       t.EVENTREFERENCE,
       t.EVENTCOMMENT,
       t.EVENTENTRYTYPE,
       t.CREATIONDATETIME
FROM   DB2ADMIN.TREPURCHASEORDEREVENTDATA t
FETCH FIRST 100 ROWS ONLY;
```
