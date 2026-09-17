# DB2ADMIN.WRKFINDOCUMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 52
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `FINANCIALYEARCODE`, `DOCUMENTTEMPLATECODE`, `STATISTICALGROUPCODE`, `DOCUMENTCODE`, `LINENUMBER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181303

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 3 | `DOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `FINANCEMONTHCODE` | INTEGER | NOT NULL |  |  |  |
| 5 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 6 | `DOCUMENTCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 8 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 9 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `GLCODE` | CHAR(20) |  |  |  |  |
| 11 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 12 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 15 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 16 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 17 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 18 | `COMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 19 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 20 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 21 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 22 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 23 | `REFERENCETEXT1` | CHAR(50) |  |  |  |  |
| 24 | `REFERENCETEXT2` | CHAR(50) |  |  |  |  |
| 25 | `REFERENCETEXT3` | CHAR(50) |  |  |  |  |
| 26 | `REFERENCETEXT4` | CHAR(50) |  |  |  |  |
| 27 | `REFERENCEAMT1` | DECIMAL(18,5) |  |  |  |  |
| 28 | `REFERENCEAMT2` | DECIMAL(18,5) |  |  |  |  |
| 29 | `REFERENCEAMT3` | DECIMAL(18,5) |  |  |  |  |
| 30 | `REFERENCEAMT4` | DECIMAL(18,5) |  |  |  |  |
| 31 | `REFERENCEAMT5` | DECIMAL(18,5) |  |  |  |  |
| 32 | `HABSVERSIONNUMBER` | BIGINT | NOT NULL |  |  |  |
| 33 | `DOCUMENTDATE` | DATE |  |  |  |  |
| 34 | `POSTINGDATE` | DATE |  |  |  |  |
| 35 | `CHEQUENUMBER` | CHAR(20) |  |  |  |  |
| 36 | `CHEQUEDATE` | DATE |  |  |  |  |
| 37 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 38 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 39 | `BUSINESSUNITDESC` | VARCHAR(200) |  |  |  |  |
| 40 | `PROFITCENTERDESC` | VARCHAR(200) |  |  |  |  |
| 41 | `COSTCENTERDESC` | VARCHAR(200) |  |  |  |  |
| 42 | `GLDESC` | VARCHAR(200) |  |  |  |  |
| 43 | `PLANTINVOICEDATA` | VARCHAR(255) |  |  |  |  |
| 44 | `PURCHASEINVOICEDATA` | VARCHAR(255) |  |  |  |  |
| 45 | `POADVANCEDATA` | VARCHAR(255) |  |  |  |  |
| 46 | `MRNDATA` | VARCHAR(255) |  |  |  |  |
| 47 | `COMMERCIALINVOICEDATA` | VARCHAR(255) |  |  |  |  |
| 48 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 49 | `DOCUMENTTYPEDESC` | VARCHAR(200) |  |  |  |  |
| 50 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 51 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINDOCUMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECODE,
       t.FINANCEMONTHCODE,
       t.STATISTICALGROUPCODE,
       t.DOCUMENTCODE,
       t.LINENUMBER,
       t.CREATIONTIMESTAMP,
       t.LINETEMPLATECODE,
       t.GLCODE,
       t.CURRENTSTATUS
FROM   DB2ADMIN.WRKFINDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
