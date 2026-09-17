# DB2ADMIN.TREWRKPURCHASEORDEREVENTDATA

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `EVENTCODE`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69594

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `EVENTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `EVENTDESCRIPTION` | VARCHAR(40) |  |  |  |  |
| 8 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 9 | `SEQUENCEDATA` | DECIMAL(5,0) |  |  |  |  |
| 10 | `EVENTDATE` | DATE |  |  |  |  |
| 11 | `EVENTTIME` | TIME |  |  |  |  |
| 12 | `EVENTNOTE` | VARCHAR(100) |  |  |  |  |
| 13 | `EVENTREFERENCE` | VARCHAR(100) |  |  |  |  |
| 14 | `EVENTCOMMENT` | VARCHAR(3000) |  |  |  |  |
| 15 | `MANDATORYEVENT` | SMALLINT | NOT NULL |  |  |  |
| 16 | `EVENTENTRYTYPE` | CHAR(1) |  |  |  |  |
| 17 | `EVENTEXIST` | SMALLINT | NOT NULL |  |  |  |
| 18 | `MANUALENTRY` | SMALLINT | NOT NULL |  |  |  |
| 19 | `AUTOMATICENTRY` | SMALLINT | NOT NULL |  |  |  |
| 20 | `ERRORFLOW` | SMALLINT | NOT NULL |  |  |  |
| 21 | `CRTDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `CRTUSER` | CHAR(25) |  |  |  |  |
| 23 | `UPDDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `UPDUSER` | CHAR(25) |  |  |  |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDER_PURCHASEORDER` | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE` | [`PURCHASEORDER`](../PURCHASING/PURCHASEORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `TREWRKPURCHASEORDEREVENTDATA.PURCHASEORDERCOMPANYCODE = PURCHASEORDER.COMPANYCODE AND TREWRKPURCHASEORDEREVENTDATA.PURCHASEORDERCOUNTERCODE = PURCHASEORDER.COUNTERCODE AND TREWRKPURCHASEORDEREVENTDATA.PURCHASEORDERCODE = PURCHASEORDER.CODE` |
| `TREPURCHASEORDEREVENT_EVENT` | `PURCHASEORDERCOMPANYCODE`, `EVENTCODE` | [`TREPURCHASEORDEREVENT`](../PURCHASING/TREPURCHASEORDEREVENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREWRKPURCHASEORDEREVENTDATA.PURCHASEORDERCOMPANYCODE = TREPURCHASEORDEREVENT.COMPANYCODE AND TREWRKPURCHASEORDEREVENTDATA.EVENTCODE = TREPURCHASEORDEREVENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREWRKPURORDEREVENTDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.PURCHASEORDERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.EVENTCODE,
       t.EVENTDESCRIPTION,
       t.SEQUENCE,
       t.SEQUENCEDATA,
       t.EVENTDATE,
       t.EVENTTIME
FROM   DB2ADMIN.TREWRKPURCHASEORDEREVENTDATA t
FETCH FIRST 100 ROWS ONLY;
```
