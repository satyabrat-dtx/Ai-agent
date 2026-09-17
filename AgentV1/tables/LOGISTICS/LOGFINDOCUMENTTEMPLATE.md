# DB2ADMIN.LOGFINDOCUMENTTEMPLATE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 91
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175066

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(3) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `DOCUMENTTYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `VALID` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ALLOWEDSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 9 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 10 | `DIRECTENTRYALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `LINESCOUNTERRATE` | INTEGER | NOT NULL |  |  |  |
| 12 | `COMMENTCRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `COMMENTALWAYSEDITABLE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CHECKDATECODE` | CHAR(20) |  |  |  |  |
| 15 | `CHECKDOCUMENTCODE` | CHAR(20) |  |  |  |  |
| 16 | `STATISTICALCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 17 | `EXCHANGERATETYPE` | INTEGER | NOT NULL |  |  |  |
| 18 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 19 | `PROJECTCONTROL` | SMALLINT | NOT NULL |  |  |  |
| 20 | `REFTEXT1` | CHAR(20) |  |  |  |  |
| 21 | `REFTEXT2` | CHAR(20) |  |  |  |  |
| 22 | `REFTEXT3` | CHAR(20) |  |  |  |  |
| 23 | `REFTEXT4` | CHAR(20) |  |  |  |  |
| 24 | `REFTEXT5` | CHAR(20) |  |  |  |  |
| 25 | `REFAMT1` | CHAR(20) |  |  |  |  |
| 26 | `REFAMT2` | CHAR(20) |  |  |  |  |
| 27 | `REFAMT3` | CHAR(20) |  |  |  |  |
| 28 | `REFAMT4` | CHAR(20) |  |  |  |  |
| 29 | `REFAMT5` | CHAR(20) |  |  |  |  |
| 30 | `FIRSTUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 31 | `FIRSTUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 32 | `SECONDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `SECONDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 34 | `THIRDUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `THIRDUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 36 | `FOURTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `FOURTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 38 | `FIFTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `FIFTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 40 | `USEDFORAP` | SMALLINT | NOT NULL |  |  |  |
| 41 | `USEDFORAPOPTION` | CHAR(2) | NOT NULL |  |  |  |
| 42 | `USEDFORAR` | SMALLINT | NOT NULL |  |  |  |
| 43 | `USEDFORAROPTION` | CHAR(2) | NOT NULL |  |  |  |
| 44 | `USEDFORMATERIAL` | SMALLINT | NOT NULL |  |  |  |
| 45 | `USEDFORMATERIALOPTION` | CHAR(2) | NOT NULL |  |  |  |
| 46 | `PAYMENTTERMS` | SMALLINT | NOT NULL |  |  |  |
| 47 | `BASEDATEDEFINITION` | CHAR(2) |  |  |  |  |
| 48 | `DUEDAYS` | INTEGER | NOT NULL |  |  |  |
| 49 | `USEDFORBANK` | SMALLINT | NOT NULL |  |  |  |
| 50 | `CHEQUEOPTION` | INTEGER | NOT NULL |  |  |  |
| 51 | `USEDFOREMPLOYEE` | SMALLINT | NOT NULL |  |  |  |
| 52 | `EMPLOYEEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 53 | `EMPLOYEEADVANCEREQUEST` | SMALLINT | NOT NULL |  |  |  |
| 54 | `ADVANCETYPE` | SMALLINT | NOT NULL |  |  |  |
| 55 | `USEDFOROTHERVENDOR` | SMALLINT | NOT NULL |  |  |  |
| 56 | `VENDORREFERENCENUMBER` | SMALLINT | NOT NULL |  |  |  |
| 57 | `VENDORREFERENCEDATE` | SMALLINT | NOT NULL |  |  |  |
| 58 | `USEDFOROTHERCUSTOMER` | SMALLINT | NOT NULL |  |  |  |
| 59 | `CUSTOMERREFERENCENUMBER` | SMALLINT | NOT NULL |  |  |  |
| 60 | `CUSTOMERREFERENCEDATE` | SMALLINT | NOT NULL |  |  |  |
| 61 | `USEDFORFOREXGAINORLOSS` | SMALLINT | NOT NULL |  |  |  |
| 62 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 63 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 64 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 65 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 66 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 67 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 68 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 69 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 70 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 71 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 72 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 73 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 74 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 75 | `WFMAPPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 76 | `DIGITALSIGNATUREALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 77 | `USINGFORADVANE` | CHAR(1) |  |  |  |  |
| 78 | `SIXTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 79 | `SIXTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 80 | `SEVENTHUSERGRPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 81 | `SEVENTHUSERGRPCODE` | CHAR(3) |  |  |  |  |
| 82 | `DIRECTINVOICEPOSTINGBY` | CHAR(1) |  |  |  |  |
| 83 | `USEDFOREXPORTFINANCE` | SMALLINT | NOT NULL |  |  |  |
| 84 | `EXPORTFINANCEOPTIONS` | CHAR(1) |  |  |  |  |
| 85 | `USEDFORLCPOSTING` | SMALLINT | NOT NULL |  |  |  |
| 86 | `LCPOSTINGOPTIONS` | CHAR(1) |  |  |  |  |
| 87 | `USEDFORLCPAYMENT` | SMALLINT | NOT NULL |  |  |  |
| 88 | `LCPAYMENTOPTIONS` | CHAR(1) |  |  |  |  |
| 89 | `USEDFORLOANS` | SMALLINT | NOT NULL |  |  |  |
| 90 | `LOANSOPTIONS` | CHAR(1) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINDOCUMENT**.`ABSUNIQUEID` (high confidence — name = 'LOGFINDOCUMENT' + known child suffix 'TEMPLATE')
  - JOIN predicate: `LOGFINDOCUMENTTEMPLATE.FATHERID = LOGFINDOCUMENT.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.DOCUMENTTYPECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.VALID,
       t.ALLOWEDSTATUS,
       t.LOGMANAGEMENT,
       t.TERMSOFLOGCODE,
       t.DIRECTENTRYALLOWED,
       t.LINESCOUNTERRATE
FROM   DB2ADMIN.LOGFINDOCUMENTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
