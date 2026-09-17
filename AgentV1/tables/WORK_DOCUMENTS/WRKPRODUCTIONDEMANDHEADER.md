# DB2ADMIN.WRKPRODUCTIONDEMANDHEADER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80313

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `PRODUCTIONDEMANDCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 7 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 8 | `ORDERPARTNERFISCALCODE` | CHAR(16) |  |  |  |  |
| 9 | `ORDERPARTNERCOUNTRYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `ORDPRNCOUNTRYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 11 | `ORDERPARTNERLEGALNAME1` | VARCHAR(200) | NOT NULL |  |  |  |
| 12 | `ORDERPARTNERLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 13 | `ORDERPARTNERADDRESSLINE1` | VARCHAR(200) | NOT NULL |  |  |  |
| 14 | `ORDERPARTNERADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 15 | `ORDERPARTNERADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 16 | `ORDERPARTNERPOSTALCODE` | CHAR(20) |  |  |  |  |
| 17 | `ORDERPARTNERTOWN` | VARCHAR(200) |  |  |  |  |
| 18 | `ORDERPARTNERDISTRICT` | VARCHAR(200) |  |  |  |  |
| 19 | `ORDERPARTNERTRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 20 | `ORDPRNTRANSPORTZONELONGDES` | VARCHAR(200) |  |  |  |  |
| 21 | `ITEMDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 22 | `COMPANYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 24 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `STOCKTYPELONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `ENTRYWAREHOUSEDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.CREATIONUSER,
       t.PRODUCTIONDEMANDCOMPANYCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.LANGUAGECODE,
       t.ORDERPARTNERFISCALCODE,
       t.ORDERPARTNERCOUNTRYCODE,
       t.ORDPRNCOUNTRYLONGDESCRIPTION,
       t.ORDERPARTNERLEGALNAME1
FROM   DB2ADMIN.WRKPRODUCTIONDEMANDHEADER t
FETCH FIRST 100 ROWS ONLY;
```
