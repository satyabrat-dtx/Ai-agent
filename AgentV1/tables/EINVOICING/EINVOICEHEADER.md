# DB2ADMIN.EINVOICEHEADER

- **Module**: `EINVOICING` (high confidence — table name starts with 'EINVOIC')
- **Roles**: `business_data`
- **Columns**: 94
- **Primary key**: `COMPANYCODE`, `UNIQUEID`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236823

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `FLOWTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `RETRYATTEMPTS` | INTEGER | NOT NULL |  |  |  |
| 4 | `EISTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `EISENTDATE` | DATE |  |  |  |  |
| 6 | `RECEIPTDATEFROMAUTHORITY` | DATE |  |  |  |  |
| 7 | `FILENAME` | CHAR(50) |  |  |  |  |
| 8 | `UNIQUEIDFROMTRANSMITTER` | CHAR(50) |  |  |  |  |
| 9 | `SDIID` | CHAR(20) |  |  |  |  |
| 10 | `TRANSMITTERCOUNTRYID` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `TRATERTAXREGISTRATIONNUMBER` | CHAR(28) | NOT NULL |  |  |  |
| 12 | `TRANSMISSIONID` | CHAR(10) |  |  |  |  |
| 13 | `TRANSMISSIONFORMAT` | CHAR(5) | NOT NULL |  |  |  |
| 14 | `RECIPIENTCODE` | CHAR(7) | NOT NULL |  |  |  |
| 15 | `TRANSMITTERPHONE` | CHAR(12) |  |  |  |  |
| 16 | `TRANSMITTEREMAIL` | VARCHAR(256) |  |  |  |  |
| 17 | `RECIPIENTEMAIL` | VARCHAR(256) |  |  |  |  |
| 18 | `SENDERCOUNTRYID` | CHAR(2) | NOT NULL |  |  |  |
| 19 | `SENDERTAXREGISTRATIONNUMBER` | CHAR(28) | NOT NULL |  |  |  |
| 20 | `SENDERFISCALCODE` | CHAR(16) |  |  |  |  |
| 21 | `SENDERDESCRIPTION` | VARCHAR(160) |  |  |  |  |
| 22 | `SENDERFIRSTNAME` | VARCHAR(120) |  |  |  |  |
| 23 | `SENDERLASTNAME` | VARCHAR(120) |  |  |  |  |
| 24 | `SENDERTITLE` | CHAR(20) |  |  |  |  |
| 25 | `SENDEREORICODE` | CHAR(17) |  |  |  |  |
| 26 | `SENDERTAXREGIMECODE` | CHAR(4) |  | FK | foreign_key |  |
| 27 | `SENDERADDRESS` | VARCHAR(120) | NOT NULL |  |  |  |
| 28 | `SENDERNUMBER` | CHAR(8) |  |  |  |  |
| 29 | `SENDERPOSTALCODE` | CHAR(5) | NOT NULL |  |  |  |
| 30 | `SENDERTOWN` | VARCHAR(120) | NOT NULL |  |  |  |
| 31 | `SENDERDISTRICT` | CHAR(2) |  |  |  |  |
| 32 | `SENDERLOCATIONCOUNTRYCODE` | CHAR(2) | NOT NULL |  |  |  |
| 33 | `WITHSENDERPERMESTABLISHMENT` | SMALLINT | NOT NULL |  |  |  |
| 34 | `SENDERPERMESTADDRESS` | VARCHAR(120) |  |  |  |  |
| 35 | `SENDERPERMESTABLISHMENTNUMBER` | CHAR(8) |  |  |  |  |
| 36 | `SENDERPERMESTPOSTALCODE` | CHAR(5) |  |  |  |  |
| 37 | `SENDERPERMESTABLISHMENTTOWN` | VARCHAR(120) |  |  |  |  |
| 38 | `SENDERPERMESTDISTRICT` | CHAR(2) |  |  |  |  |
| 39 | `SENDERPERMESTCOUNTRYCODE` | CHAR(2) |  |  |  |  |
| 40 | `REA` | SMALLINT | NOT NULL |  |  |  |
| 41 | `REAOFFICECODE` | CHAR(2) |  | FK | foreign_key |  |
| 42 | `REANUMBER` | CHAR(20) |  |  |  |  |
| 43 | `REASHARECAPITAL` | DECIMAL(14,2) |  |  |  |  |
| 44 | `REAUNIQUEPARTNER` | CHAR(2) |  |  |  |  |
| 45 | `REALIQUIDATION` | CHAR(2) |  |  |  |  |
| 46 | `WITHSENDERCONTACTS` | SMALLINT | NOT NULL |  |  |  |
| 47 | `SENDERPHONE` | CHAR(12) |  |  |  |  |
| 48 | `SENDERFAX` | CHAR(12) |  |  |  |  |
| 49 | `SENDEREMAIL` | VARCHAR(256) |  |  |  |  |
| 50 | `WITHSENDERREPRESENTATIVE` | SMALLINT | NOT NULL |  |  |  |
| 51 | `SENDERREPRESENTATIVECOUNTRYID` | CHAR(2) |  |  |  |  |
| 52 | `SENDERREPRTAXREGNUMBER` | CHAR(28) |  |  |  |  |
| 53 | `SENDERREPRESENTATIVEFISCALCODE` | CHAR(16) |  |  |  |  |
| 54 | `SENDERREPRDESCRIPTION` | VARCHAR(160) |  |  |  |  |
| 55 | `SENDERREPRESENTATIVEFIRSTNAME` | VARCHAR(120) |  |  |  |  |
| 56 | `SENDERREPRESENTATIVELASTNAME` | VARCHAR(120) |  |  |  |  |
| 57 | `SENDERREPRESENTATIVETITLE` | CHAR(20) |  |  |  |  |
| 58 | `SENDERREPRESENTATIVEEORICODE` | CHAR(17) |  |  |  |  |
| 59 | `RECIPIENTCOUNTRYID` | CHAR(2) | NOT NULL |  |  |  |
| 60 | `RECIPIENTTAXREGISTRATIONNUMBER` | CHAR(28) | NOT NULL |  |  |  |
| 61 | `RECIPIENTFISCALCODE` | CHAR(16) |  |  |  |  |
| 62 | `RECIPIENTDESCRIPTION` | VARCHAR(160) |  |  |  |  |
| 63 | `RECIPIENTFIRSTNAME` | VARCHAR(120) |  |  |  |  |
| 64 | `RECIPIENTLASTNAME` | VARCHAR(120) |  |  |  |  |
| 65 | `RECIPIENTTITLE` | CHAR(20) |  |  |  |  |
| 66 | `RECIPIENTEORICODE` | CHAR(17) |  |  |  |  |
| 67 | `RECIPIENTADDRESS` | VARCHAR(120) | NOT NULL |  |  |  |
| 68 | `RECIPIENTNUMBER` | CHAR(8) |  |  |  |  |
| 69 | `RECIPIENTPOSTALCODE` | CHAR(5) | NOT NULL |  |  |  |
| 70 | `RECIPIENTTOWN` | VARCHAR(120) | NOT NULL |  |  |  |
| 71 | `RECIPIENTDISTRICT` | CHAR(2) |  |  |  |  |
| 72 | `RECIPIENTLOCATIONCOUNTRYCODE` | CHAR(2) | NOT NULL |  |  |  |
| 73 | `WITHRECIPIENTPERMEST` | SMALLINT | NOT NULL |  |  |  |
| 74 | `RECIPIENTPERMESTADDRESS` | VARCHAR(120) |  |  |  |  |
| 75 | `RECIPIENTPERMESTNUMBER` | CHAR(8) |  |  |  |  |
| 76 | `RECIPIENTPERMESTPOSTALCODE` | CHAR(5) |  |  |  |  |
| 77 | `RECIPIENTPERMESTTOWN` | VARCHAR(120) |  |  |  |  |
| 78 | `RECIPIENTPERMESTDISTRICT` | CHAR(2) |  |  |  |  |
| 79 | `RECIPIENTPERMESTCOUNTRYCODE` | CHAR(2) |  |  |  |  |
| 80 | `WITHRECIPIENTREPRESENTATIVE` | SMALLINT | NOT NULL |  |  |  |
| 81 | `RECIPIENTREPRCOUNTRYID` | CHAR(2) |  |  |  |  |
| 82 | `RECIPIENTREPRTAXREGNUMBER` | CHAR(28) |  |  |  |  |
| 83 | `RECIPIENTREPRDESCRIPTION` | VARCHAR(160) |  |  |  |  |
| 84 | `RECIPIENTREPRFIRSTNAME` | VARCHAR(120) |  |  |  |  |
| 85 | `RECIPIENTREPRLASTNAME` | VARCHAR(120) |  |  |  |  |
| 86 | `ISSUER` | CHAR(2) |  |  |  |  |
| 87 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 88 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 89 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 90 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 91 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 92 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 93 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EINVOICEHEADER.COMPANYCODE = COMPANY.CODE` |
| `ITALIANDISTRICT_REAOFFICE` | `REAOFFICECODE` | [`ITALIANDISTRICT`](../EINVOICING/ITALIANDISTRICT.md) | `CODE` | RESTRICT | `EINVOICEHEADER.REAOFFICECODE = ITALIANDISTRICT.CODE` |
| `TAXREGIME_SENDERTAXREGIME` | `SENDERTAXREGIMECODE` | [`TAXREGIME`](../EINVOICING/TAXREGIME.md) | `CODE` | RESTRICT | `EINVOICEHEADER.SENDERTAXREGIMECODE = TAXREGIME.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EINVOICEHEADER_BODY` | [`EINVOICEBODY`](../EINVOICING/EINVOICEBODY.md) | `EINVOICEHEADERCOMPANYCODE`, `EINVOICEHEADERUNIQUEID` | `EINVOICEBODY.EINVOICEHEADERCOMPANYCODE = EINVOICEHEADER.COMPANYCODE AND EINVOICEBODY.EINVOICEHEADERUNIQUEID = EINVOICEHEADER.UNIQUEID` |

## Indexes

- `EINVOICEHEADERUID` (ABSUNIQUEID)
- `EINVOICEHEADER1` (COMPANYCODE, FLOWTYPE, UNIQUEIDFROMTRANSMITTER)
- `EINVOICEHEADER2` (COMPANYCODE, FILENAME, FLOWTYPE)
- `EINVOICEHEADER3` (COMPANYCODE, FLOWTYPE, TRANSMISSIONID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANYCODE,
       t.FLOWTYPE,
       t.RETRYATTEMPTS,
       t.EISTATUS,
       t.EISENTDATE,
       t.RECEIPTDATEFROMAUTHORITY,
       t.FILENAME,
       t.UNIQUEIDFROMTRANSMITTER,
       t.SDIID,
       t.TRANSMITTERCOUNTRYID,
       t.TRATERTAXREGISTRATIONNUMBER
FROM   DB2ADMIN.EINVOICEHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
