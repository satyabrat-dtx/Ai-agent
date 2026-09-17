# DB2ADMIN.WRKLOOMSTICKERPRINTINGFORARV

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `COMPANYCODE`, `ENTRYDATE`, `SHIFTCODE`, `DEMANDCOUNTERCODE`, `DEMANDCODE`, `ROLLNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131097

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `IPLOOMNO` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `IPDATE` | DATE | NOT NULL |  |  |  |
| 6 | `IPSHIFTNO` | INTEGER | NOT NULL |  |  |  |
| 7 | `IPDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `IPDEMANDCODE` | CHAR(15) |  |  |  |  |
| 9 | `PLANTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `CUSTOMERNAME` | VARCHAR(200) |  |  |  |  |
| 11 | `ENTRYDATE` | DATE | NOT NULL | PK | primary_key |  |
| 12 | `PARTIALCOMPLETEDPC` | CHAR(3) |  |  |  |  |
| 13 | `SHIFTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 14 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 16 | `SOLINE` | DECIMAL(7,0) |  |  |  |  |
| 17 | `SOSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `SOCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 19 | `SODELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 20 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 21 | `PRODUCTIONORDERQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 22 | `PRODUCTIONORDERQTY` | DECIMAL(15,5) |  |  |  |  |
| 23 | `DEMANDCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 24 | `DEMANDCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 25 | `PRODUCTIONCATEGORY` | CHAR(20) |  |  |  |  |
| 26 | `PRODUCTID` | CHAR(10) |  |  |  |  |
| 27 | `ROLLNO` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 28 | `LOOMNO` | CHAR(10) |  |  |  |  |
| 29 | `SIZESETNO` | CHAR(30) |  |  |  |  |
| 30 | `QUANTITYUOMCODE` | CHAR(3) |  |  |  |  |
| 31 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 32 | `DYEDYARNLOTNO` | CHAR(50) |  |  |  |  |
| 33 | `WARPSUPPLIER` | CHAR(20) |  |  |  |  |
| 34 | `FIRSTROLL` | CHAR(3) |  |  |  |  |
| 35 | `WEFTMIX` | CHAR(20) |  |  |  |  |
| 36 | `WEFTSUPPLIER` | CHAR(20) |  |  |  |  |
| 37 | `POCOMPLETIONDATE` | DATE | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.COMPANYCODE,
       t.IPLOOMNO,
       t.WORKCENTERCODE,
       t.IPDATE,
       t.IPSHIFTNO,
       t.IPDEMANDCOUNTERCODE,
       t.IPDEMANDCODE,
       t.PLANTDESCRIPTION,
       t.CUSTOMERNAME,
       t.ENTRYDATE
FROM   DB2ADMIN.WRKLOOMSTICKERPRINTINGFORARV t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
