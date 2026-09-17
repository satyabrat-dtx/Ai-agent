# DB2ADMIN.VALUEDWAREHOUSEPRINTWORK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `NUMBERID`, `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 12041

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NUMBERID` | INTEGER | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 7 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 8 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 16 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 17 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) |  |  |  |  |
| 18 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 19 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 20 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 21 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 22 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) |  |  |  |  |
| 23 | `PERIODCODE` | DECIMAL(3,0) |  |  |  |  |
| 24 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `LASTACCOUNTCLOSUREDATE` | DATE |  |  |  |  |
| 26 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `COSTIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 28 | `LASTINBOUNDCOST` | DECIMAL(18,5) |  |  |  |  |
| 29 | `LASTINBOUNDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 30 | `STANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 31 | `STANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 32 | `WEIGHTEDAVERAGECOST` | DECIMAL(18,5) |  |  |  |  |
| 33 | `BASECOSTUNITCODE` | CHAR(3) |  |  |  |  |
| 34 | `DYNAMICAVERAGECOSTTOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `DYNAMICAVERAGECOSTTOTALQTY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `DYNAMICAVERAGECOST` | DECIMAL(18,5) |  |  |  |  |
| 37 | `HIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 38 | `HIFOCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 39 | `SECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 40 | `SNDSTANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 41 | `FIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 42 | `FIFOCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 43 | `LIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 44 | `LIFOCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 45 | `NUMBEROFDECIMALS` | INTEGER | NOT NULL |  |  |  |
| 46 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 47 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 48 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 49 | `WHSACCOUNTINGGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 50 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.NUMBERID,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.ITEMTYPECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06
FROM   DB2ADMIN.VALUEDWAREHOUSEPRINTWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
