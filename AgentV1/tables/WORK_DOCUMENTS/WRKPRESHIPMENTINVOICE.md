# DB2ADMIN.WRKPRESHIPMENTINVOICE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 48
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `CREATIONUSER`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145484

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 3 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 4 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `LINETOEXPLODE` | INTEGER | NOT NULL |  |  |  |
| 6 | `SDLSALDOCPRVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `SDLSALDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 8 | `SDLORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 9 | `SDLORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `SDLCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 13 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 15 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 16 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `RELEASECODE` | CHAR(15) |  |  |  |  |
| 26 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 28 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 29 | `SECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 30 | `PACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 31 | `PACKAGEUOMCODE` | CHAR(3) |  |  |  |  |
| 32 | `INVOICEQTY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 36 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 38 | `LOTCODE` | CHAR(15) |  |  |  |  |
| 39 | `LENGTH` | DECIMAL(7,2) |  |  |  |  |
| 40 | `WIDTH` | DECIMAL(7,2) |  |  |  |  |
| 41 | `HEIGHT` | DECIMAL(7,2) |  |  |  |  |
| 42 | `REMARKS` | VARCHAR(200) |  |  |  |  |
| 43 | `ALLOCATED` | SMALLINT | NOT NULL |  |  |  |
| 44 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 45 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 46 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 47 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINENO,
       t.LINETOEXPLODE,
       t.SDLSALDOCPRVCOUNTERCODE,
       t.SDLSALDOCUMENTPROVISIONALCODE,
       t.SDLORDERLINE,
       t.SDLORDERSUBLINE,
       t.SDLCOMPONENTORDERLINE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE
FROM   DB2ADMIN.WRKPRESHIPMENTINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
