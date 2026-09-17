# DB2ADMIN.LOGFINPAYMENTPROPOSALLINE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 57
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227420

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPAYMENTPROPOSALCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINPAYMENTPROPOSALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `ODLBUSINESSUNITCODE` | CHAR(10) | NOT NULL |  |  |  |
| 3 | `ODLFINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL |  |  |  |
| 4 | `ODLDOCUMENTTEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `ODLSTATISTICALGROUPCODE` | CHAR(6) | NOT NULL |  |  |  |
| 6 | `ODLCODE` | CHAR(15) | NOT NULL |  |  |  |
| 7 | `ODLLINENUMBER` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `AMOUNTTOCLEAR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 11 | `PDLBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 12 | `PDLFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 13 | `PDLDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 14 | `PDLSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 15 | `PDLCODE` | CHAR(15) |  |  |  |  |
| 16 | `PDLLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 17 | `OPTDSTDSTEUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 18 | `OPTDSTDSTYPECODE` | CHAR(10) |  |  |  |  |
| 19 | `OPTDSTDSCODE` | CHAR(6) |  |  |  |  |
| 20 | `OPTDSTDSITAXCODE` | CHAR(3) |  |  |  |  |
| 21 | `OPTDSEXEMPTIONFROMDATE` | DATE |  |  |  |  |
| 22 | `TDSPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 23 | `TDSAPPLICABLEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 24 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 25 | `TDSGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `TDSGLCODE` | CHAR(20) |  |  |  |  |
| 27 | `TDLBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 28 | `TDLFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 29 | `TDLDOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 30 | `TDLSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 31 | `TDLCODE` | CHAR(15) |  |  |  |  |
| 32 | `TDLLINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 33 | `PURCHASEINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 34 | `PURINVOICEORDPRNCSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 35 | `PURINVOICEORDPRNCSMSUPCODE` | CHAR(8) |  |  |  |  |
| 36 | `PURCHASEINVOICECODE` | CHAR(25) |  |  |  |  |
| 37 | `PURCHASEINVOICEINVOICEDATE` | DATE |  |  |  |  |
| 38 | `DIRECTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 39 | `DIRECTINVOICECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 40 | `DIRECTINVOICECODE` | CHAR(15) |  |  |  |  |
| 41 | `INVOICEDATE` | DATE |  |  |  |  |
| 42 | `INVOICENO` | CHAR(25) |  |  |  |  |
| 43 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 44 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 45 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 46 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 47 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 48 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 49 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 50 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 51 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 52 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 53 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 54 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 55 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 56 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINPAYMENTPROPOSAL**.`ABSUNIQUEID` (high confidence — name = 'LOGFINPAYMENTPROPOSAL' + known child suffix 'LINE')
  - JOIN predicate: `LOGFINPAYMENTPROPOSALLINE.FATHERID = LOGFINPAYMENTPROPOSAL.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINPAYMENTPROPOSALCOMPANYCODE,
       t.FINPAYMENTPROPOSALCODE,
       t.ODLBUSINESSUNITCODE,
       t.ODLFINANCIALYEARCODE,
       t.ODLDOCUMENTTEMPLATECODE,
       t.ODLSTATISTICALGROUPCODE,
       t.ODLCODE,
       t.ODLLINENUMBER,
       t.AMOUNTTOCLEAR,
       t.ORDERPARTNERTYPE,
       t.ORDERPARTNERCODE,
       t.PDLBUSINESSUNITCODE
FROM   DB2ADMIN.LOGFINPAYMENTPROPOSALLINE t
FETCH FIRST 100 ROWS ONLY;
```
