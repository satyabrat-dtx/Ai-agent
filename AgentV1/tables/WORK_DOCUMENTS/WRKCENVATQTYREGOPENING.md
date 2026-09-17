# DB2ADMIN.WRKCENVATQTYREGOPENING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 46
- **Primary key**: `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `CREATIONTIMESTAMP`, `RECORDTYPE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144337

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `EXCISEYEARREGNO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `EXCISEYEARCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 4 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 5 | `RECORDTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 8 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `MRNMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 10 | `MRNCODE` | DECIMAL(11,0) |  |  |  |  |
| 11 | `MRNDATE` | DATE |  |  |  |  |
| 12 | `REPORTFROM` | DATE |  |  |  |  |
| 13 | `REPORTTO` | DATE |  |  |  |  |
| 14 | `INVOICENO` | CHAR(15) |  |  |  |  |
| 15 | `INVOICEDATE` | DATE |  |  |  |  |
| 16 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `PRODUCTCODE` | CHAR(50) |  |  |  |  |
| 19 | `PRODUCTDESC` | CHAR(50) |  |  |  |  |
| 20 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 21 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 22 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 23 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 24 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 25 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 26 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 27 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 28 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 29 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `QUANTITYUMCODE` | CHAR(3) |  |  |  |  |
| 31 | `OPCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 32 | `OPCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 33 | `MRNLINENETTAMT` | DECIMAL(18,5) |  |  |  |  |
| 34 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 36 | `OBQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `DRQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `CRQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `CLQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `DOCUMENTNO` | CHAR(30) |  |  |  |  |
| 41 | `SUPPLIERNAME` | VARCHAR(80) |  |  |  |  |
| 42 | `RANGECODE` | CHAR(15) |  |  |  |  |
| 43 | `RANGEDIVISIONCODE` | CHAR(15) |  |  |  |  |
| 44 | `RANGEDIVISIONDESCRIPTION` | CHAR(100) |  |  |  |  |
| 45 | `ECCNO` | CHAR(30) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.EXCISEYEARREGNO,
       t.EXCISEYEARCODE,
       t.CREATIONTIMESTAMP,
       t.RECORDTYPE,
       t.LINENO,
       t.TARIFFCODE,
       t.CODE,
       t.MRNMRNPREFIXCODE,
       t.MRNCODE,
       t.MRNDATE
FROM   DB2ADMIN.WRKCENVATQTYREGOPENING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
