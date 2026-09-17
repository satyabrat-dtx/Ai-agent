# DB2ADMIN.WRKMSESPECIFICATIONPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 94153

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `PHASE` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `SPECIFICATIONGROUPCODE` | CHAR(3) |  |  |  |  |
| 5 | `SPECIFICATIONHEADERCODE` | CHAR(3) |  |  |  |  |
| 6 | `SPECIFICATIONTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `SPECMASTERDEFINITIONCODE` | CHAR(3) |  |  |  |  |
| 8 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 10 | `VALIDITYFROMDATE` | DATE |  |  |  |  |
| 11 | `VALIDITYTODATE` | DATE |  |  |  |  |
| 12 | `CHECKEDOK` | SMALLINT | NOT NULL |  |  |  |
| 13 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 14 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 15 | `FULLITEMDESCR` | VARCHAR(200) |  |  |  |  |
| 16 | `TRANSACTIONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `LINEVALUE` | INTEGER | NOT NULL |  |  |  |
| 18 | `LINEMAXVALUE` | INTEGER | NOT NULL |  |  |  |
| 19 | `TEMPLATETOTALVALUE` | INTEGER | NOT NULL |  |  |  |
| 20 | `TEMPLATEMAXVALUE` | INTEGER | NOT NULL |  |  |  |
| 21 | `TEMPLATEWEIGHTEDTOTALVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 22 | `TEMPLATEWEIGHTEDMAXVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 23 | `HEADERTOTALVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 24 | `HEADERMAXVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 25 | `GROUPTOTALVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 26 | `GROUPMAXVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 27 | `PERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 28 | `CLASSIFICATIONCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 29 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 30 | `QATRANSACTION` | CHAR(50) |  |  |  |  |
| 31 | `ROWTYPE` | CHAR(2) |  |  |  |  |
| 32 | `LINEVALUEQTY` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 33 | `LINEMAXVALUEQTY` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 34 | `ROWDATE` | DATE |  |  |  |  |
| 35 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 36 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 37 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 38 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 39 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 40 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.COMPANYCODE,
       t.PHASE,
       t.SPECIFICATIONGROUPCODE,
       t.SPECIFICATIONHEADERCODE,
       t.SPECIFICATIONTEMPLATECODE,
       t.SPECMASTERDEFINITIONCODE,
       t.SUPPLIERTYPE,
       t.SUPPLIERCODE,
       t.VALIDITYFROMDATE,
       t.VALIDITYTODATE
FROM   DB2ADMIN.WRKMSESPECIFICATIONPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
