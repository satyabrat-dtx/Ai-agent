# DB2ADMIN.WRKNETCOSTSHEETAPPROVAL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 31
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 200398

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SALORDLINESALORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `SALESORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `SALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `SALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 7 | `SALORDLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 21 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 22 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 23 | `APPROVALDATE` | DATE |  |  |  |  |
| 24 | `COSTPERUNIT` | DECIMAL(18,5) |  |  |  |  |
| 25 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 26 | `SELLINGPRICE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 28 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 29 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 30 | `RECORDSTATUS` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.SALORDLINESALORDERCOUNTERCODE,
       t.SALESORDERLINESALESORDERCODE,
       t.SALESORDERLINEORDERLINE,
       t.SALESORDERLINEORDERSUBLINE,
       t.SALORDLINECOMPONENTORDERLINE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02
FROM   DB2ADMIN.WRKNETCOSTSHEETAPPROVAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
