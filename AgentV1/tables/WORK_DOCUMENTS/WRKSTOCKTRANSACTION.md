# DB2ADMIN.WRKSTOCKTRANSACTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CREATIONUSER`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 147372

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 5 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 6 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 10 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 11 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 12 | `BASESECONDARYUNITCODE` | CHAR(3) |  |  |  |  |
| 13 | `PRODUCTCODE` | CHAR(140) |  |  |  |  |
| 14 | `PRODUCTDESC` | CHAR(100) |  |  |  |  |
| 15 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 16 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 17 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 18 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 19 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 20 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 21 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 22 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 23 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `ZONECODE` | CHAR(20) |  |  |  |  |
| 25 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 26 | `DISTRIBUTERNAME` | CHAR(15) |  |  |  |  |
| 27 | `SHADELOT` | CHAR(2) |  |  |  |  |
| 28 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 29 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 30 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 31 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LINENO,
       t.ITEMTYPECODE,
       t.ITEMELEMENTCOMPANYCODE,
       t.ITEMELEMENTSUBCODEKEY,
       t.ITEMELEMENTCODE,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.CONTAINERELEMENTCOMPANYCODE,
       t.CONTAINERELEMENTCODE,
       t.BASEPRIMARYUNITCODE,
       t.BASEPRIMARYQUANTITYUNIT
FROM   DB2ADMIN.WRKSTOCKTRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
