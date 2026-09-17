# DB2ADMIN.WRKINTERNALHEADER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `INTERNALORDERCOMPANYCODE`, `INTERNALORDERCOUNTERCODE`, `INTERNALORDERCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34732

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `INTERNALORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `INTERNALORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `INTERNALORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 7 | `ORDERPARTNERFISCALCODE` | CHAR(16) |  |  |  |  |
| 8 | `ORDERPARTNERCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 9 | `ORDPRNCOUNTRYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `ORDERPARTNERLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 11 | `ORDERPARTNERLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 12 | `ORDERPARTNERADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 13 | `ORDERPARTNERADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 14 | `ORDERPARTNERADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 15 | `ORDERPARTNERPOSTALCODE` | CHAR(20) |  |  |  |  |
| 16 | `ORDERPARTNERTOWN` | VARCHAR(200) |  |  |  |  |
| 17 | `ORDERPARTNERDISTRICT` | VARCHAR(200) |  |  |  |  |
| 18 | `ORDERPARTNERTRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 19 | `ORDPRNTRANSPORTZONELONGDES` | VARCHAR(200) |  |  |  |  |
| 20 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 21 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 22 | `DELIVERYCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `DLVTRANSPORTZONELONGDES` | VARCHAR(200) |  |  |  |  |
| 24 | `COMPANYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 25 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 26 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `TERMSOFDLVLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `TERMSOFSHPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 29 | `FIRSTCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `SECONDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `THIRDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.INTERNALORDERCOMPANYCODE,
       t.INTERNALORDERCOUNTERCODE,
       t.INTERNALORDERCODE,
       t.LANGUAGECODE,
       t.ORDERPARTNERFISCALCODE,
       t.ORDERPARTNERCOUNTRYCODE,
       t.ORDPRNCOUNTRYLONGDESCRIPTION,
       t.ORDERPARTNERLEGALNAME1,
       t.ORDERPARTNERLEGALNAME2
FROM   DB2ADMIN.WRKINTERNALHEADER t
FETCH FIRST 100 ROWS ONLY;
```
